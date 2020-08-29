import pygame
import  sys
from pygame.locals import *

pygame.init()



WHITE=(255,255,255) 
BLACK=(0,0,0)

size=width,height=600,250
screen=pygame.display.set_mode(size)
pygame.display.set_caption("fish")

clock=pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()


    screen.fill(WHITE)
    pygame.draw.rect(screen,BLACK,(50,50,150,50),0)  #画出来三个矩形
    pygame.draw.rect(screen,BLACK,(250,50,150,50),1)
    pygame.draw.rect(screen,BLACK,(450,50,150,50),10)


    pygame.display.flip()  #把矩形显示出来


    clock.tick(10)   #一秒钟绘制10次
