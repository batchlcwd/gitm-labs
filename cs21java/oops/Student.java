
import java.util.List;

class Student {
    // class body

    // properties
    String name;
    String phone;
    String address;
    String rollnumber;
    String collegeName;
    int age;
    boolean isActive;
    String notActiveReason;
    // List<String> list;

    // methods // functionalies
    void showCollegeName() {
        // kaam...
        System.out.println("College name " + collegeName);

    }

    void showDetail() {
        // NAME
        System.out.println("Name: " + name);
        System.out.println("Phone: " + phone);
        System.out.println("Address: " + address);
        System.out.println("Age : " + age);
        System.out.println("Rollnumber: " + rollnumber);
        System.out.println("user is active : " + isActive);
        if (!isActive) {
            System.out.println(notActiveReason);
        }
    }

    // method equals()
    public boolean equals(Object ob2) {
        // logic: object comparision
        // this
        Student student1 = this;
        Student student2 = (Student) ob2;
        return (student1.name.equals(student2.name) && student1.rollnumber.equals(student2.rollnumber));
    }

}