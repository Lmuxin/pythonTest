import pygame
import sys
from pygame.locals import *


pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("F:\\ybw.Ogg")
pygame.mixer.music.set_volume(0.2)  #音量
pygame.mixer.music.play()


cat_sound=pygame.mixer.Sound("F:\\ll.Ogg")
cat_sound.set_volume(0.2)



dog_sound=pygame.mixer.Sound("F:\\lsh.Ogg")
dog_sound.set_volume(0.2)







bg_size=width,height=300,200
screen=pygame.display.set_mode(bg_size)

pygame.display.set_caption("music")


pause=False



clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            sys.exit()

        if event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                cat_sound.play()
            if event.button==3:
                dog_sound.play()
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
                pause=not pause
    screen.fill(255,255,255)

    pygame.display.flip()

    clock.tick(30)

   
        
                          
