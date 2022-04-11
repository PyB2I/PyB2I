
from farm.fowl import Fowl as Fowl

class Chicken(Fowl) :
    u""" Chicken definition """
    def __init__(self, name = "Pollo anónimo ...") :
        Fowl.__init__(self, name)
        return

    
    def __str__(self) :
        return "soy un pollo mi nombre es " + Fowl.__str__(self)

    
    def greet(self) :
        return "pio pio"
    