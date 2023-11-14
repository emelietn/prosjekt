#dino
from figur import Figur

class Dino(Figur):
    def __init__(self, bildesti: str, gravitasjon: int, hopp: str) -> None:
        super().__init__("bilder/dino1.png")
        self.gravitasjon = gravitasjon
        self.hopp = hopp

    
    def gravitasjon(self):
        self.gravitasjon = 0.1


    def hopp(self):
        self.hopp
    
    