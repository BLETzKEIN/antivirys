import time

import pygame,random
#qwe=pygame.Surface([300,300])
qwe=pygame.image.load("SKAR.jpg")
qws=pygame.image.load("zhyk.png")
qwe=pygame.transform.scale(qwe,[1200,700])
qws=pygame.transform.scale(qws,[50,100])
qwe=pygame.transform.flip(qwe,True,False)
qwe.blit(qws,[50,280])
# pygame.draw.line(qwe,[39,94,125],[0,0],[299,299],20)
# qwe.fill([57,98,180])
pygame.image.save(qwe,"2.jpg")
a=pygame.display.set_mode([1200,700])
# print(a)
# a.fill([52,70,68])
wile=0
while True:
    time.sleep(1/60)
    pygame.event.get()
    a.blit(qwe,[0,0])
    wile=wile+1
#     a.fill([52,70,69])
#     pygame.draw.polygon(a,[52,70,170],[[100,100],[wile,200],[200,500],[600,wile]],1)
#     pygame.draw.circle(a,[49,175,90],[wile,wile],100,10)
#     pygame.draw.rect(a,[99,100,250],[100,200,wile,400],10)
#     pygame.draw.line(a,[200,78,208],[wile,wile],[1000,500],20)
#     pygame.draw.ellipse(a,[67,206,190],[100,200,wile,400],35)
#     pygame.draw.arc(a,[90,245,159],[wile/2,wile/2,300,wile/2],0,wile*0.0174533,13)
    pygame.display.flip()
#     pygame.image.save(a,"3.jpg")