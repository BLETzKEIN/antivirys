import random
import time

import pygame

qwerty = [
    28,
    56,
    112
]
print(qwerty[1])

a = pygame.display.set_mode([1500, 750])
pygame.init()


f=pygame.font.SysFont("arial",30,True,True)
q=f.render("ia ryssiy",True,[255,0,0])
pygame.image.save(q,"text.png")

qwe = pygame.Rect(200, 100, random.randint(100, 150), random.randint(100, 150))
qwe1 = pygame.Rect(40, 100, random.randint(50, 80), random.randint(50, 80))
qwe2 = pygame.Rect(0, 0, a.get_width(), a.get_height())
qwe10 = pygame.Rect(0, 0,700, 500)
qwe6 = pygame.Rect(0, 0,1000, 600)
qwe3 = pygame.Rect(0, 0, 500, 400)
qwe4 = pygame.Rect(0, 0, 200, 200)
qwe5 = pygame.Rect(0, 0, 300, 300)
qwe.centerx = 1400 / 2
qwe.centery = 700 / 2
qwer = 0

spisok = [
    [qwe2, 0, 0],
    [qwe6,3,3],
    [qwe10,5,1],
    [qwe3, 2, 4],
    [qwe5,3,2],
    [qwe4,4,1],
    [qwe, 3, 1],
    [qwe1,3,4]
]



def move(nbig, nsmall):
    n2=spisok[nsmall]
    rect_small=n2[0]
    speedx=n2[1]
    speedy=n2[2]

    n1=spisok[nbig]
    rect_big=n1[0]
    speedx_big=n1[1]
    speedy_big=n1[2]

    rect_small.centery+=speedy_big
    rect_small.centery += speedy



    if rect_small.bottom > rect_big.bottom:
        rect_small.bottom = rect_big.bottom
        speedy = -speedy
        n2[2]=speedy
    if rect_small.top < rect_big.top:
        rect_small.top = rect_big.top
        speedy = -speedy
        n2[2] = speedy

    rect_small.centerx+=speedx_big
    rect_small.centerx += speedx

    if rect_small.left < rect_big.left:
        rect_small.left = rect_big.left
        speedx = -speedx
        n2[1] = speedx

    if rect_small.right > rect_big.right:
        rect_small.right = rect_big.right
        speedx = -speedx
        n2[1] = speedx
    if len(spisok)-1>=nsmall+1:
        move(nsmall,nsmall+1)



while True:
    time.sleep(1 / 100)
    pygame.event.get()

    move(0,1)



    a.fill([50, 50, 50])
    qwsd = 30
    # pygame.draw.rect(a,[200,150,200],qwe2)
    # pygame.draw.rect(a, [qwe.x%256, qwe.y%256, abs(qwe.x-qwe.y)%256], qwe)
    for o in spisok:
        qwsd += 20
        pygame.draw.rect(a, [qwsd, qwsd / 2, 256 - qwsd], o[0])
    a.blit(q, [0, 0])
    pygame.display.flip()
