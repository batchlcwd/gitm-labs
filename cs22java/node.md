## Basics ✅

    jshell
    program
    variables

## Data Type ✅

    byte
    short
    char
    int
    float
    long
    double
    boolean

## How to write and run java program

1. Create a file and write code=> Source Code

2. Compile Source Code

   bytecode

3. Run the program[byte]

sourcecode-->compile[javac filename.java]-->bytecode[java classname]--->run-->output

Rule to create java program:

1. create a class

class [classame]
{//class opening

// statements inside class

}//class closing

keywords: special words whose meaning is known to compiler.
eg
class,for,if,else,while,static etc.

Identifier: User/Programmer defined words
eg
classname
variable name
function/method name

Rules to create idenfiers: 1. combination
A-Z
a-z
0-9
but identifiers can not start form digits

    2. No special symbols are allowed exception $ and _

    3. keywords can not used as identifiers

    4. [indentifiers]class name/ interface name used as identifier

2. functions / methods

jitte marzi --->

create a main method:

public static void main(String arr[])
{
//statements
}

## Type Casting / Type Conversion

Converting one type value to another type value.

### Automatic Conversion/ Implicit TypeCasting/ Widening TC

autmatically convert types [jre]
conversion karte samay data loss nhi hota hai to

### Forceful Conversion / Explicit Type Casting / Narrowing TC

Forcefully convert types by programmer
conversion data loss ho raha hai

## Class and Ojects / Object Oriented Programming System.

- What is class? ✅
- What is Object?✅
- How to create object✅
- Attribute✅
- Methods✅
- method overloading✅
- constructor✅
- constructor overloading✅
- Programs:
- 1.Class which represent point
- have basics operations
- 1.)find_distance of two point
- 2.)ditance from x-axis and y-axis
- 3.)find co-ordinat of point
- 2.class which represnt complex number
- have basics operations
  4- Complex number

## Constructor Overloading:

Whenever we create more than one construtor inside classs then this is called Constructor Overloading.

Conditions:

- Arugument **list** must different:
  - Number of parameters different
  - Type of parameter different
  - Order of parameter different

## Method Overloading:

Whenever we will create more than 1 method with same name and with different argument list. Then this is method overloading.

- Condition of method overloading
- method name must be same
- argument must be different
  - number of parameters
  - type of parameters
  - order of parameters

### Advantages of Method Overlaoding:

Compile Time Polymorphism/ static binding

```java
public class Calculator {

    void add(int x, int y) {
        System.out.println(x + y);
    }

    void add(int x, int y, int z) {
        System.out.println(x + y + z);
    }

    void add(int x, int y, int z, int a) {
        System.out.println(x + y + z + a);
    }

    void add(int... x) {
        int s = 0;
        for (int h : x) {
            s = s + h;
        }
        System.out.println(s);
    }
}


```

Calling overloaded method

```java
public class CalcEx {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        calculator.add(2, 3);
        calculator.add(3, 3, 3);
        calculator.add(4, 4, 4, 4);
        calculator.add(5, 5, 5, 5, 5, 5);

    }
}


```

## Inheritance:
