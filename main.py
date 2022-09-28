import pygame, sys
from random import randint
from pygame.locals import QUIT
import pygame.gfxdraw
import colmap
w,h = 400,300
dw,dh = 400,30
pygame.init()
img= pygame.image.load("unnamed.png")
def rndcol():
  return (
    randint(0,255),
    randint(0,255),
    randint(0,255)
  )
scr = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
while True:
  scr.fill((0,0,0))
  for x in range(dw):
    for y in range(dh):
      col = rndcol()
      pygame.gfxdraw.pixel(scr,x,y,col)
      for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
      pygame.display.update()
  break
colmap.surfToColmap("cols.colmap",scr)
colmap.surfToColmap("img.colmap",img)

surf = colmap.load("cols.colmap")
scr.blit(surf,(0,0))
pygame.display.update()