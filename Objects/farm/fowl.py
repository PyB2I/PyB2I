
from farm.animal import Animal as Animal

class Fowl(Animal) :
    u""" Fowl definition """
    def __init__(self, name = "Ave sin nombre ...") :
        Animal.__init__(self, name)
        return
