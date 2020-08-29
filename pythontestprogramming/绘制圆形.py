import pygame
import  sys
from pygame.locals import *

pygame.init()



WHITE=(255,255,255) 
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)


size=width,height=600,250
screen=pygame.display.set_mode(size)
pygame.display.set_caption("fish")


position=size[0]//2,size[1]//2

moving=False


clock=pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()

        if event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                moving=True
        if event.type==MOUSEBUTTONUP:
            if event.button==1:
                moving=False
    if moving:
        position=pygame.mouse.get_pos()
        
                

            
    screen.fill(WHITE)
    pygame.draw.circle(screen,RED,position,25,1)  #画出来个圆形
    pygame.draw.circle(screen,GREEN,position,75,1)
    pygame.draw.circle(screen,BLUE,position,125,1) 
  
    pygame.display.flip()  #把矩形显示出来


    clock.tick(10)   #一秒钟绘制10次
