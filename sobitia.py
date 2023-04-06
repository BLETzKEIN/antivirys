import random

import pygame

pygame.init()

a = pygame.display.set_mode([1400, 700])

f = pygame.font.SysFont("arial", 30, True, True)
q = f.render("НЕ ЗАКРОЮСЬ!", True, [255, 0, 0])
spaace = f.render("ПрОбЕл", True, [0, 255, 250])
filli = f.render("автоматическая очистка каждые 10 секунд", True, [255, 255, 255])

nomertimer = pygame.event.custom_type()
pygame.time.set_timer(nomertimer, 10000)

while True:
    b = pygame.event.get()
    for u in b:
        if u.type == pygame.QUIT:
            a.blit(q, [650, 300])

        if u.type == pygame.KEYDOWN:
            if u.key == pygame.K_SPACE:
                a.blit(spaace, [random.randint(50, 1200), random.randint(50, 650)])
            else:
                keyy = f.render("клавиша " + str(u.key), True, [0, 200, 200])
                a.blit(keyy, [random.randint(50, 1300), random.randint(50, 650)])
        if u.type == pygame.MOUSEBUTTONDOWN:
            if u.button == pygame.BUTTON_LEFT:
                mish = f.render("мышь "+str(u.pos),True,[126,245,72])
                a.blit(mish,u.pos)
            elif u.button == pygame.BUTTON_RIGHT:
                mish = f.render("мышь " + str(u.pos), True, [235, 150, 89])
                a.blit(mish, u.pos)
            else:
                mish = f.render("мышь " + str(u.pos), True, [0, 255, 210])
                a.blit(mish, u.pos)

        if u.type == nomertimer:
            a.fill([0, 0, 0])
            a.blit(filli, [0, 0])

    pygame.display.flip()
