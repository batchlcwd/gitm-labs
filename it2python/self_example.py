class Example:
    def __init__(self):
        self.x=45
        self.name="INTIAL OBJECT"
    
    def show_name(self):
        print(self)
        print(self.name)

ob1=Example()
ob2=Example()
ob3=Example() 
ob1.name='object1'
ob2.name='object2'
ob3.name='object3'
print(ob1)
ob1.show_name()
print(ob2)
ob2.show_name()
# ob3.show_name()

