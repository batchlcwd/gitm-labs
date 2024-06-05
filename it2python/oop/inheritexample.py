class Dadaji:
    def __init__(self):
        self.x=100


class Papaji(Dadaji):
    def __init__(self):
        self.y=400
        Dadaji.__init__(self)

class Ham(Papaji):
    def __init__(self):
        self.z=10
        # parent class constructor 
        Papaji.__init__(self)

# dada=Dadaji()
# papa = Papaji()
ham=Ham() 


print(ham.x)
print(ham.y)
print(ham.z)
