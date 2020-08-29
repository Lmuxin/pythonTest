import pygame
import  sys
import math
from pygame.locals import *
from random import *

#球类继承自Sprite类
class Ball(pygame.sprite.Sprite):
    def __init__(self,image,position,speed,bg_size):
        #初始化动画精灵
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load(image).convert_alpha()
        self.rect=self.image.get_rect()
        #把小球放在指定位置
        self.rect.left,self.rect.top=position
        self.speed=speed
        self.width,self.height=bg_size[0],bg_size[1]
        self.radius=self.rect.width/2 

    def move(self):
       self.rect=self.rect.move(self.speed)

        #如果小球的左侧出了边界,小球左侧的位置改为右侧的边界
       #这样实现了从左边进入,右边出来的效果
       if self.rect.right<0:
           self.rect.left=self.width
           
       elif self.rect.left>self.width:
            self.rect.right=0

       elif self.rect.bottom<0:
               self.rect.top=self.height
               
       elif self.rect.top>self.height:
               self.rect.bottom=0

def collide_check(item,target):
    col_balls=[]
    for each in target:
            distance=math.sqrt(math.pow((item.rect.center[0]-each.rect.center[0]),2)\
                      + math.pow((item.rect.center[1]-each.rect.center[1]),2))
            if distance<=(item.rect.width+each.rect.width)/2:
                col_balls.append(each)

    return col_balls




class Galss(pygame.sprite.Sprite):
    def __init__(self,glass_image,mouse_image,bg_size):
        #初始化动画精灵
        pygame.sprite.Sprite.__init__(self)
        self.glss_image=pygame.image.load(glass_image).convert_alpha()
        self.glass_rect=self.glasss.get_rect()
        self.glass_rect.left,self.glass_rect.top=\
                                                  (bg_size[0]-self.glass_tect.width)//2,\
                                                      bg_size[1]-self.glass_rect.height


        self.mouse_image=pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect=self.mouse.get_rect()
        self.mouse_rect.leftself.gmouse_rect.top=\
                                                  bself.glass_rect.left,self.glass_rect.top
        pygame.mouse.set_visible(False)
                                                   
        
        


def main():


        pygame.init()

        glass_image="F:\\codephoto\\h.png"
        mouse_image="F:\\codephoto\\3.png"
        ball_image='F:\\codephoto\\g.png'
        bg_image='F:\\codephoto\\2.gif'

        running=True
      #添加背景音乐
        pygame.mixer.music.load("F:\\ybw.Ogg")
        pygame.mixer.music.play()

   #添加音效

        loser_sound=pygame.mixer.Sound("F:\\ll.Ogg")

        winner_sound=pygame.mixer.Sound("F:\\ll.Ogg")

        #音乐播完时游戏结束
        GAMEOVER=USEREVENT
        pygame.mixer.music.set_endevent(GAMEOVER)




        #根据北京图片大小指定游戏界面尺寸
        bg_size=width,height=1024,681
        screen=pygame.display.set_mode(bg_size)
        pygame.display.set_caption("play the ball")


        background=pygame.image.load(bg_image).convert_alpha()

#用来存放小球对象的列表
        balls=[]
        group=pygame.sprite.Group()
        




        
        #创建5个小球
        BALL_NUM=5
       
            
        for i in range(5):
            #位置随机,速度随机
            position=randint(0,width-100),randint(0,height-100)
            speed=[randint(-10,10),randint(-10,10)]
            ball=Ball(ball_image,position,speed,bg_size)
            

            while pygame.sprite.spritecollide(ball,group,False,pygame.sprite.collide_circle):
                ball.rect.left,ball.rect.top=randint(0,width-100),randint(0,height-100)

            
           # while collide_check(ball,balls):
            #  ball.rect.left,ball.rect.top=randint(0,width-100),randint(0,height-100)
                
            balls.append(ball)
            group.add(ball)


        glass=Glass(glass_image,mouse_imagebg_size)
        clock=pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type==QUIT:
                    sys.exit()

                elif event.type==GAMEOVER:
                    loser_sound.play()
                    pygame.time.delay(2000)
                    running=False
                    
                    

                screen.blit(background,(0,0))
                screen.blit(glass.glass_image,glass.glass_rect)

                glass.mouse_rect.left,glass.rect.top=pygame.mouse.get_pos()
                if glass.mouse_rect.left<glass.glass_rect.left:
                    glass.mouse_rect.left=glass.glass_rect.left
                if glass.mouse_rect.left>glass.glass_rect.right-glass.mouse_rect.width:
                    glass.mouse_rect.left=glass.glass_rect.right-glass.mouse_rect.width
                if glass.mouse_rect.top<glass.glass_rect.top:
                    glass.mouse_rect.top=glass.glass_rect.top
                if glass.mouse_rect.top<glass.glass_rect.bottom-glass.mouse_rect.height:
                    glass.mouse_rect.top=glass.glass_rect.bottom-glass.mouse_rect.height
                     
                    


                screen.blit(glass.mouse_image,glass.mouse_rect)




                
                 


                for each in balls:
                    each.move()
                    screen.blit(each.image,each.rect)

                for each in group:
                    group.remove(each)

                    if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_circle):
                            each.speed[0]=-each.speed[0]
                            each.speed[1]=-each.speed[1]


                    group.add(each)
                        

               # for i in range(BALL_NUM):
                #    item=balls.pop(i)

                   # if collide_check(item,balls):
                   #     item.speed[0]=-item.speed[0]
                        #item.speed[1]=-item.speed[1]

                 #   balls.insert(i,item)
                        
                



                pygame.display.flip()
                clock.tick(30)
                


              
if __name__=="__main__":
        main()
