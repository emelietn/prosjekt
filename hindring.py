#hindringer
from figur import Figur

class Hindring(Figur):
    def __init__(self, bildesti: str, topp: int, venstre: int) -> None:
        super().__init__(bildesti)
        self.fart = -2
        self.ramme.top = topp
        self.ramme.left = venstre

    def beveg(self):
        self.ramme.left += self.fart
        if self.ramme.right < 0:
            self.ramme.left = 600
            self.fart -= 0.1





        

    



