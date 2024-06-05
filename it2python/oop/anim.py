class Animal:
   
    def __init__(self,name):
      self.name=name

    def eat(self):
      print(self.name," is eating")

class Dog(Animal):
   def __init__(self):
      self.color='black'
    #   Animal.__init__(self)
      super().__init__('DOG')


class Cat(Animal):
   def __init__(self,name):
          super().__init__(name)

dog=Dog()

dog.eat()

print(dog.color)

cat =Cat("CAT ABC13415")
cat.eat()

cat =Cat("CAT 36346")
cat.eat()