# class Student:
#     pass 
class Student:

    # properties/variales
    # behaviours/methods
    # initialize
    # constructor 
    def __init__(self,name,phone,college):
        print("creating object")
        self.name=name
        self.phone=phone
        self.college=college

    def display_all(self):
        print("Name ",self.name)
        print("College ",self.college)
        print("Phone ",self.phone)


# Object Creation:
# print("creating object")  
# this is calling constructor
student1=Student("Amar",2424242,"GITM")

student2=Student("Sachin",2525235,"BBD")

# student1.name='Amar'
# student1.college="GITM"
# student1.phone=4141414
# print(student1.name)
# print(student1.college)
student1.display_all()
# student2.name="Sachin"
# student2.college="BBD"
# student2.phone=2425
student2.display_all()

