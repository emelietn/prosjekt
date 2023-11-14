import pygame
from hindring import Hindring
from dino import Dino

pygame.init()

BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

#dino
dino = Dino("bilder/dino1.png")
dino.ramme.top = 405


#bakgrunn
bakgrunn_x = 0
bakgrunn_y = 500
bakgrunn_bilde = pygame.image.load("bilder/bakgrunn.png").convert_alpha()
bakgrunn_fart = -2




while True:
    #2.hondter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            pygame.quit()
            raise SystemExit
        
    #bagrunnen
    bakgrunn_x -=1
    if bakgrunn_x < -200:
        bakgrunn_x = 0


    taster = pygame.key.get_pressed()

    #3 oppdater spill

    #4 tegn

    vindu.fill("white")
    vindu.blit(bakgrunn_bilde, (bakgrunn_x, bakgrunn_y))
    dino.tegn(vindu)
    

    pygame.display.flip()
    klokke.tick(FPS) 