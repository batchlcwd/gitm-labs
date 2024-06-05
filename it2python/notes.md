# Functions

Set of statements written for doing a specific task.

- name
- parameters
- return value

- in order to run the function we have call the function

- function without arguemnt and return type

- function with argument
- function with argument and return type
- function with default values

- function with named arguent
- variable arugment function

## Practice programs

1. WAP to print all the prime numbers between 1 to 100 using functions

2. change 1 to 100 with dynamic range.

# Class and Object

## Object:

    Object is an real world enitity.
    which can be seen , touched, etc.

1. - properties/data members/object variables
2. - behaviours/ member methods/methods
   - it real world entity

## Class:

    Blueprint of an object from which object can be created.

- it is a logical entity

## Constructor

- Special methods of class used to initlized objects.
- special name
  ```python
  def __init__(self):
      pass
  ```

## self keyword:

self refer current invoking object.

## overloding

- Creating more than one method with same name in same class.
- Python doest not supprot overloading

## Inheritance

- what is inheritance
- how inhertance
- calling constructor from child - class
- super()

- Example

```python
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

```
