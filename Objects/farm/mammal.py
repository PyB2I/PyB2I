
from farm.animal import Animal as Animal

class Mammal(Animal) :
    u""" Mammal definition """
    def __init__(self, name = "Mamifero sin nombre ...") :
        Animal.__init__(self, name)
        return

