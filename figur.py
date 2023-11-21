#figur.py
import pygame

class Figur():
    def __init__(self, bildesti: str) -> None:
        self.bilde = pygame.image.load(bildesti)
        self.ramme = self.bilde.get_rect()

    def tegn(self, bakgrunn: pygame.Surface):
        bakgrunn.blit(self.bilde, self.ramme)

    
    