#dino
from figur import Figur

class Dino(Figur):
    def __init__(self, bildesti: str, gravitasjon: int) -> None:
        super().__init__("bilder/dino1.png")
        self.gravitasjon = gravitasjon


    
    def gravitasjon(self):
        self.gravitasjon = 0.1

    def løper(self):
        pass

    def dukk(self):
        pass


    def hopp(self):
        pass
    
    