import random
import time

import pygame

a=pygame.display.set_mode([1400,700])

def romb(x,y,size,qw):
    # pygame.draw.line(a, [69, 230, 105], [200, 200], [350, 350], 2)
    # pygame.draw.line(a, [69, 230, 105], [350, 350], [200, 500], 2)
    # pygame.draw.line(a, [69, 230, 105], [200, 500], [50, 350], 2)
    # pygame.draw.line(a, [69, 230, 105], [50, 350], [200, 220], 2)
    pygame.draw.circle(a,[69, 230, 105],[x,y],qw)
    pygame.draw.line(a,[69, 230, 105],[x,y-size],[x+size,y],qw)
    pygame.draw.line(a,[69, 230, 105],[x+size,y],[x,y+size],qw)
    pygame.draw.line(a,[69, 230, 105],[x,y+size],[x-size,y],qw)
    pygame.draw.line(a,[69, 230, 105],[x-size,y],[x,y-size+10],qw)

    if size>10 and qw>=2:
        romb(x,y,size-10,qw-1)

while True:
    time.sleep(2)
    pygame.event.get()
    # a.fill([0,0,0])
    romb(random.randint(50,1350),random.randint(50,650),random.randint(50,150),random.randint(7,10))


    pygame.display.flip()