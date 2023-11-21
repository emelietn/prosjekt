import pygame
from figur import Figur

class Meny(Figur):
    def __init__(self) -> None:
        self.font = pygame.font.SysFont('arial', 40)
        self.title = self.font.render('My Game', True, (255, 255, 255))

    def knapp(self, tekst: str):
        return self.font.render(tekst, True, ("black"))
    

    def tegn_start_meny(self, vindu):
        vindu.fill("white")
        vindu.blit(self.knapp("trykk space for å begynne spillet!"),(20, 300))


    def game_over_meny(self, vindu, higscore):
        vindu.fill("white")
        highscore_surface = self.font.render(f"Highest Score: {higscore}", True, "black")
        vindu.blit(highscore_surface, (20, 450))
        vindu.blit(self.knapp("game over"), (20, 300))
       
