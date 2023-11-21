import pygame

class Dino:
    def __init__ (self):
        self.bilde1 = pygame.image.load("bilder/dino1.png").convert_alpha()
        self.bilde2 = pygame.image.load("bilder/dino2.png").convert_alpha()
        self.bildedukk1 = pygame.image.load("bilder/dinodukk1.png").convert_alpha()

        self.gravitasjon = 0.1
        self.rect = self.bilde1.get_rect()

    

#1.oppsett
pygame.init()

BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
stor_font = pygame.font.SysFont("Arial", 24)
liten_font = pygame.font.SysFont("Arial", 12)

#Dinoen/spiller

gtravitasjon = 0.1
dino_x = 10
dino_y = 300
dino_y_fart = 0
dino_bilde1 = pygame.image.load("bilder/dino1.png").convert_alpha()
dino_bilde2 = pygame.image.load("bilder/dino2.png").convert_alpha()
dinodukk_bilde1 = pygame.image.load("bilder/dinodukk1.png").convert_alpha()
dino_bilde = dino_bilde1
dino_rect = dino_bilde.get_rect()

#bakgrunn
bakgrunn_x = 0
bakgrunn_y = 500
bakgrunn_bilde = pygame.image.load("bilder/bakgrunn.png").convert_alpha()
bakgrunn_fart = -2


#kaktus
kaktus2 = pygame.image.load("bilder/tre2.png").convert_alpha()
kaktus1 = pygame.image.load("bilder/tre1.png").convert_alpha()
kaktus_surface = kaktus1
kaktus_rect = kaktus_surface.get_rect()
kaktus_rect.left = BREDDE
kaktus_rect.bottom = 520
kaktus_fart = -2

#fugl
fugl1 = pygame.image.load("bilder/fugl1.png").convert_alpha()
fugl2 = pygame.image.load("bilder/fugl2.png").convert_alpha()
fugl_surface = fugl1
fugl_rect = fugl_surface.get_rect()
fugl_rect.left = BREDDE
fugl_rect.top = 300
fugl_fart = -2

while True:
    #2.hondter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            pygame.quit()
            raise SystemExit
        
    taster = pygame.key.get_pressed()

    if taster[pygame.K_UP]:
        dino_y_fart = -2
        dino_y -= 5
        

    if dino_y > 410:
        dino_y_fart = 0
    else:
        dino_y_fart += gtravitasjon
        dino_y += dino_y_fart
    

    
    if taster[pygame.K_DOWN]:
        dino_bilde = dinodukk_bilde1
        

    if taster[pygame.K_ESCAPE]:
        pygame.quit()
        raise SystemExit

    #3.oppdater spill


    kaktus_rect.left += kaktus_fart
    if kaktus_rect.right < 0:
        if kaktus_surface == kaktus2:
            kaktus_surface = kaktus1

            
        elif kaktus_surface == kaktus1:
            kaktus_surface = kaktus2
        kaktus_rect.left = BREDDE

  
    fugl_rect.left += fugl_fart
    if fugl_rect.right < 0:
        if fugl_surface == fugl2:
            fugl_surface = fugl1
        elif fugl_surface == fugl1:
            fugl_surface = fugl2
            fugl_rect.left = BREDDE

    #bagrunnen
        bakgrunn_x -=1
        if bakgrunn_x < -200:
            bakgrunn_x = 0

    #kollisjon
    if dino_rect.colliderect(kaktus_rect):
        print("Game over")
        pygame.quit()
        raise SystemExit

    #4. tegn
    vindu.fill("white")
    vindu.blit(dino_bilde, (dino_x, dino_y))
    vindu.blit(bakgrunn_bilde, (bakgrunn_x, bakgrunn_y))
    vindu.blit(kaktus_surface, (kaktus_rect))
    vindu.blit(fugl_surface, (fugl_rect))
    
    pygame.display.flip()
    klokke.tick(FPS)