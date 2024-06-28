## Data Types

Primitive Data types
Inbuilt programing language

1. byte
   1 byte-- 8 bits
2. short
   2 byte- 16 bits
3. char
   2 byte - 16 bits  
   single characters 'A', 'B'
4. int
   4 byte = 32 bits --> integer values
5. float
   4 byte = 32 bits --> decimal values
6. double
   8 byte = 64 bits --> decimal values
7. long
   8 bytes = 64 bits --> integers
8. boolean
   1 bit == true/false

Non Primitive/ User Defined / Reference Type
User/Programmer Defined Datatypes

String, BigDecimal, BigInteger

    Desktop / c drive / d drive
    desktop>cs21java>First.java

How to run java Program
1.source code- java code likhenge

    2.code ko compile - byte code
        javac Filename.java

    3.byte code -code run karnege

        java Classname

Rules:

1.  class create

         class [className]
         {

          // code inside class

         }

    keywords : predefined words whose meaning is known to compiler.
    eg
    class, if, else, for, int, byte, flaot, long,import, package, final , static etc.

    Identifiers: User/Programmer defined words in program.

    eg. variable name
    class name
    method name

2.  if you want start a program
    main method/function

        create a main method inside java class

    public - [access from anywhere]
    static- [can be called directly without object]
    void - return nothing[main ke lie fix hai]
    main- name of method[main ke lie fix hai]
    (String args[])-argument mein array
    int x
    String args[]

    public static void main(String args[])
    {

        // code.. likhoge to wo main ke ander hoga

    }

## Type Conversion/ Type Casting

int --> float
float --> int
int --> long
long --> int
byte --> short

1. Automatic--> Implicit Type Conversion
2. Forceful --> Explicit Type Conversion

## Class and Ojects / Object Oriented Programming System.

- What is class?

  - Class is blueprint of an object.
  - It is logical entity.
  - properties/data members/ instance variables
  - behaviours/ member methods / object functionality.

- What is Object?

  1.  Object is real world entity.
  2.  object has some Properties / instance variabels
  3.  and Behaviours / member methods / methods
  4.  unique indentifer

  example: 1. bike- object
  properties / variables / data memeber
  (headlight, wheel, mirror, tyres)

  ***

  behavours/ methods / functionaliy
  (light throw karna,
  chalna,
  back side dekhna) 2. mobile phone[iphone 13 pro max]
  properties:
  camera, screen, color, speaker,
  behaviours
  photo click,
  video dekhna,
  audio sunna. 3. DOG,CAT,HUMAN
  properties,
  hand,eyes,nose,legs etc..
  behaviours
  eating, speaking, talking, walking, studying, etc. 4. laptop
  propeties
  color, shape, screen,speaker,battery etc...
  behaviours
  long lasting,
  gamming,
  music,
  recording videos,
  recording songs,
  internet surfing

- How we can create objects.:

  - Want class

- How to create object

usecase:  
 hame ek object banana , wo object aman(student) ka -->
properties
name=aman,phone,address,rollnumber,college,
methods
showCollegeName()
showDetail()

1. Create student class so that we can create object from that class.

- Attribute
- Methods
- method overloading
- constructor
- constructor overloading
- Programs:
- 1.Class which represent point
- have basics operations 1.)find_distance of two point
- 2.)ditance from x-axis and y-axis
- 3.)find co-ordinat of point
- 2.class which represnt complex number
- have basics operations

### CLASS AND OBJECT ✅

### THIS ✅

- Remove naming confliction
- this refers to current invoking object

### REFRENCE VARIABLES

### OBJECT PASSING

### WITH EXAMPLE

```java
class Point {

    // instance variables
    int x;
    int y;

    // public static final double PIE_VALUE=3.146;

    // constructor
    // it does not return any value not even void
    // constructor name must be equal to classname
    // automatically call -- object creation time

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
        System.out.println("Object Created");
    }

    // methods
    public void display() {
        System.out.println("( " + x + " , " + y + " )");

    }
    // distance method-->

    public double calculateDistance(Point p2) {
        Point p1 = this;

        double xTemp = Math.pow((p1.x - p2.x), 2);
        double yTemp = Math.pow((p1.y - p2.y), 2);
        double xYAdd = xTemp + yTemp;
        double answer = Math.sqrt(xYAdd);
        // System.out.println("Distance " + String.format("%,.2f", answer));
        return answer;

        // this
        // p1 and p2
        // distance cal
        // print
    }

    // midpoint method-->
    public Point calculateMidPoint(Point p2) {

        Point p1 = this;

        int xMid = (p1.x + p2.x) / 2;
        int yMid = (p1.y + p2.y) / 2;

        Point midPint = new Point(xMid, yMid);
        return midPint;

    }

}


```

main calling program

```java
class PointExample {
    public static void main(String[] args) {
        // 1st approch
        // int x1=45;
        // int y1=34;

        // int x2=45;
        // int y2=45;

        // 100

        // 2 approch
        // Data types--> class
        int x = 45;
        Point p1 = new Point(45, 34);
        // p1.x = 45;
        // p1.y = 34;
        p1.display();

        Point p2 = new Point(33, 11);
        // p2.x = 33;
        // p2.y = 11;

        p2.display();

        Point p3 = new Point(2, 4);
        Point p4 = new Point(20, 4);
        Point p5 = new Point(200, 4);
        Point p6 = new Point(2000, 4);
        Point p7 = new Point(21, 4);
        Point p8 = new Point(223, 4);
        p3.display();
        p4.display();
        p5.display();
        p6.display();
        p7.display();
        p8.display();

        double dis = p1.calculateDistance(p2);
        System.out.println("Distance : " + dis);

        // p6.calculateDistance(p7);

        double dis2 = p4.calculateDistance(p5);
        System.out.println("Distance " + dis2);

        Point p100 = new Point(10, 20);
        Point p101 = new Point(5, 10);

        p100.display();
        p101.display();
        Point midPoint = p100.calculateMidPoint(p101);
        midPoint.display();

        Point mPoint2 = midPoint.calculateMidPoint(p101);
        mPoint2.display();

    }
}

```

### Practice Programs

WAP to define two complex number andn perform different operations

1. Add complex numbers
2. Substract complex numbers
3. Multiply complex numbers
