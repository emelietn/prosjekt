#dino
from figur import Figur

class Dino(Figur):
    def __init__(self, bildesti: str) -> None:
        super().__init__("bilder/dino1.png")
        self.fart = 1
        self.akselerasjon = 0.2

    
    def gravitasjon(self):
        self.fart += self.akselerasjon
        

    def hopp(self):
        self.fart = -5
        
    def beveg(self):
        self.gravitasjon()
        self.ramme.y += self.fart
        if self.ramme.bottom > 530:
            self.fart = 0
        
    
    