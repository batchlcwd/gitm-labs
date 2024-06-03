class Student {
    // properties/Data Members
    int rollNumber;
    String name;
    String college;

    // constructor
    // object initialize
    Student(int r, String n, String c) {
        rollNumber = r;
        name = n;
        college = c;
        System.out.println("Object Created");
    }

    // behaviours/Methods
    void show() {

        System.out.println("Name : " + name);
        System.out.println("Rollnumber: " + rollNumber);
        System.out.printf("College : %s \n", college);

    }

}