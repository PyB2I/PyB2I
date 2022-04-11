

class Animal :
    u""" Animal definition """
    def __init__(self, name = "Animal sin nombre ...") :
        self.name = name
        return

    
    def __str__(self) :
        return self.name

    
    def greet(self) :
        pass
