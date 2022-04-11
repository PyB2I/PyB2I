
from farm.mammal import Mammal as Mammal

class Lamb(Mammal) :
    u""" Lamb definition """
    def __init__(self, name = "Cordero Jon Doe ...") :
        Mammal.__init__(self, name)
        return

    
    def __str__(self) :
        return "soy un cordero mi nombre es " + Mammal.__str__(self)

    
    def greet(self) :
        return "mee mee"
    