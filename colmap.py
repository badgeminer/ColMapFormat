import os,pygame
import pygame.gfxdraw
Ver = 1
class formatError(Exception):
  def __init__(self,file,format):
    self.file = file
    self.format = format
  def __str__(self):
    return f"{self.file} is not formated for colmap {Ver} Curent Format is for V{str(self.format)}"
    
def load(file):
  f = open(file,mode="rb")
  form = int.from_bytes(f.read(4), byteorder='big')
  if form != Ver: raise formatError(file,form)
  fw,fh = int.from_bytes(f.read(4),   byteorder='big'),int.from_bytes(f.read(4), byteorder='big')
  f.read(4)
  cols = []
  surf = pygame.Surface((fw,fh))
  for i in range(int((os.path.getsize(file)-6)/3)):
    cols.append((
    int.from_bytes(f.read(1), byteorder='big'),
    int.from_bytes(f.read(1), byteorder='big'),
    int.from_bytes(f.read(1), byteorder='big')
  ))
  I =0
  for x in range(fw):
    for y in range(fh):
      pygame.gfxdraw.pixel(surf,x,y,cols[I])
      I +=1
  return surf

def surfToColmap(file,surf):
  f = open(file,mode="wb")
  f.write(Ver.to_bytes(4, byteorder='big', signed=False))
  f.write(surf.get_width().to_bytes(4, byteorder='big', signed=False))
  f.write(surf.get_height().to_bytes(4, byteorder='big', signed=False))
  f.write((0).to_bytes(4, byteorder='big', signed=False))
  for x in range(surf.get_width()):
    for y in range(surf.get_height()):
      col = tuple(surf.get_at((x,y)))
      f.write(col[0].to_bytes(1, byteorder='big', signed=False))
      f.write(col[1].to_bytes(1, byteorder='big', signed=False))
      f.write(col[2].to_bytes(1, byteorder='big', signed=False))
  f.close()
  