
from farm.fowl import Fowl as Fowl

class Duck(Fowl) :
    u""" Duck definition """
    def __init__(self, name = "Pato desconocido ...") :
        Fowl.__init__(self, name)
        return

    
    def __str__(self) :
        return "soy un pato mi nombre es " + Fowl.__str__(self)

    
    def greet(self) :
        return "cuac cuac"
    