import pygame
import  sys
from pygame.locals import *

pygame.init()



WHITE=(255,255,255) 
BLACK=(0,0,0)
GREEN=(0,255,0)

points=[(200,75),(300,25),(400,75),(450,25),(450,125),(400,75),(300,125)]


size=width,height=600,250
screen=pygame.display.set_mode(size)
pygame.display.set_caption("fish")

clock=pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()


    screen.fill(WHITE)
    pygame.draw.polygon(screen,GREEN,points,0)  #画出来个多边形
  
    pygame.display.flip()  #把矩形显示出来


    clock.tick(10)   #一秒钟绘制10次
