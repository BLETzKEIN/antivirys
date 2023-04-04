import random
import time

import pygame
a=pygame.display.set_mode([1400,700])
qwe=pygame.Rect(200,100,random.randint(50,150),random.randint(50,150))
qwe.centerx=1400/2
qwe.centery=700/2
qwer=0
speedy=3
speedx=1

while True:
    time.sleep(1/100)
    pygame.event.get()

    qwe.centery+=speedy


    if qwe.bottom>700:
        qwe.bottom=700
        speedy=-3
    if qwe.top<0:
        qwe.top=0
        speedy=3

    qwe.centerx+=speedx


    if qwe.left<0:
        qwe.left=0
        speedx=1

    if qwe.right>1400:
        qwe.right=1400
        speedx=-1

    # qwe.centerx=qwe.centerx-1
    # if qwe.bottom<700 and qwer==0:
    #     qwe.centery+=3
    # elif qwe.bottom>700:
    #     qwe.bottom=700
    #     qwer=1
    #
    # elif qwe.top>0 and qwer==1:
    #     qwe.centery-=3
    # elif qwe.top<0:
    #     qwe.top=0
    #     qwer=0
    a.fill([50,50,50])
    pygame.draw.rect(a, [qwe.x%256, qwe.y%256, abs(qwe.x-qwe.y)%256], qwe)

    pygame.display.flip()
