import pygame
pygame.init()


f=pygame.font.SysFont("arial",30,True,True)
q=f.render("ia ryssiy",True,[46,83,251])
pygame.image.save(q,"text.png")