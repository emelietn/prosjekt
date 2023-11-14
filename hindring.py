#hindringer
from figur import Figur

class Hindring(Figur):
    def __init__(self, bildesti: str) -> None:
        super().__init__("bilder/tre1.png")
        self.fart = -2

    def beveg(self):
        self.beveg = self.fart
    



