import pygame
from hindring import Hindring
from dino import Dino
from meny import Meny

#initialiserer pygame
pygame.init()

# Definerer spillvinduets bredde, høyde og bildefrekvens per sekund (FPS)
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

#meny
meny = Meny()
spill_tilstand = "start_meny"


#poengsum
poengsum_font = pygame.font.SysFont("Arial", 32)
poengsum_surface = poengsum_font.render("poeng", True, "black")


#dino
dino = Dino("bilder/dino1.png")
dino.ramme.top = 300

#hindring
hindringer_liste = [
        
    Hindring("bilder/tre1.png", 450, 600),
    Hindring("bilder/tre2.png", 450, 1800),
    Hindring("bilder/fugl1.png", 200, 2400),
]



#bakgrunn
bakgrunn_x = 0
bakgrunn_y = 500
bakgrunn_bilde = pygame.image.load("bilder/bakgrunn.png").convert_alpha()
bakgrunn_fart = -2

#poeng
poeng = 0

#higscore
higscore = 0


# Hovedspill-løkke
while True:
    #2.hondter input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            pygame.quit()
            raise SystemExit
    

    taster = pygame.key.get_pressed()

    # Håndterer spilltilstanden "start_meny"
    if spill_tilstand ==  "start_meny":
        meny.tegn_start_meny(vindu)
        if taster [pygame.K_SPACE]:
            spill_tilstand = "spill"

    # Håndterer spilltilstanden "game_over"
    elif spill_tilstand == "game_over":
        meny.game_over_meny(vindu, higscore)
        vindu.blit(poengsum_surface, (BREDDE // 20, 400))
        if taster [pygame.K_SPACE]:


            #tilbakestiller og starter spillet på nytt hvis en trykker "space"
            dino.ramme.top = 300
            hindring.ramme.left = BREDDE
            poeng = 0
            spill_tilstand = "spill"

    # Håndterer spilltilstanden "spill"
    else: 
        if taster[pygame.K_SPACE]:
            dino.hopp()
            poeng += 1
        if poeng > higscore:
            higscore = poeng

            
        #bagrunnen
        bakgrunn_x -=1
        if bakgrunn_x < -200:
            bakgrunn_x = 0

        #hindring
        for hindring in hindringer_liste:
            hindring.beveg()


        #3 oppdater spill
        dino.beveg()
        poengsum_surface = poengsum_font.render(f"Poengsum: {poeng}",True, "black")
        

        for hindring in hindringer_liste:
            if dino.ramme.colliderect(hindring.ramme):
                spill_tilstand = "game_over"
                meny.game_over_meny(vindu, higscore)
            
    
        #4 tegn
        vindu.fill("white")
        vindu.blit(bakgrunn_bilde, (bakgrunn_x, bakgrunn_y))
        dino.tegn(vindu)
        for hindring in hindringer_liste:
            hindring.tegn(vindu)
        vindu.blit(poengsum_surface, (0,0))

        

    pygame.display.flip()
    klokke.tick(FPS) 