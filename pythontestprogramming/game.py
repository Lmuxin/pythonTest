import pygame
import sys
from pygame.locals import *


#初始化

pygame.init()


size=width,height=600,400
speed=[-2,1]
bg=(255,255,255)
fullscreen=False

#创建指定大小的窗口
screen=pygame.display.set_mode(size)

# 设置窗口标题
pygame.display.set_caption("初次见面多多关照")



#加载图片
turtle=pygame.image.load("f:\\codephoto\\c.png")


#获取图片的位置矩形

position=turtle.get_rect()

l_hear=turtle
r_head=pygame.transform.flip(turtle,True,False)


while True:
    for event in pygame.event.get():
       if event.type==pygame.QUIT:
         sys.exit()

       if event.type==KEYDOWN:
            if even.key==K_LEFT:
                turtle=l_head
                speed=[-1,0]
            if even.key==K_RIGHT:
                 turtle=r_head
                 speed=[1,0]

            if even.key==K_UP:
                speed=[0,-1]
                
            if even.key==K_DOWN:
                speed=[0,1]

            #全屏
            if event.key==k_F11:
                fullscreen=not fullscreen
                if fullscreen:
                      screen=pygame.display.set_mode((1024,768),FULLSCREEN|HWSURFACE)
                else:
                      screen=pygame.display.set_mode(size)





        
#移动图形
       position =position.move(speed)


    if position.left<0 or position.right>width:
            #翻转图形
            turtle=pygame.transform.flip(turtle,True,False)
            #反向移动
            speed[0]=-speed[0]

    if position.top<0 or position.bottom>height:
            speed[1]=-speed[-1]

            #填充背景

            screen.fill(bg)

            #更新图像

            screen.blit(turtle,position)

            #更新界面

            pygame.display.flip()

             # 延迟10毫秒

            pygame.time.delay(10)


  







            
