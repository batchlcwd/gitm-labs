class Demo {
    public static void main(String[] args) {
        //
        System.out.println("Program started:");
        // yhi par object banayenge
        // creating object:

        Student student1 = new Student();
        student1.rollnumber = "1313";
        student1.name = "Aman";
        student1.collegeName = "GITM";
        student1.phone = "235235235";
        student1.age = 23;
        student1.address = "GOMTI NAGAR";
        student1.isActive = false;
        student1.notActiveReason = "Not active for bad peformace";
        student1.showCollegeName();

        student1.showDetail();

        // student 2:

        Student student2 = new Student();

        student2.rollnumber = "1313";
        student2.name = new String("Aman");
        student2.collegeName = "BBDNITM";
        student2.age = 25;
        student2.address = "INDRA NAGAR";
        student2.phone = "235235235235";
        student2.isActive = true;
        System.out.println("______________");
        student2.showDetail();

        // i want to compare two objects
        // kis class ke objects:
        if (student1.equals(student2)) {
            System.out.println("boths objects are same");
        } else {
            System.out.println("both objects are not same");
        }

        // if (student1.name.equals(student2.name)) {
        // System.out.println("both object is same [student1 and student2]");
        // } else {
        // System.out.println("both student obect are not same [student1 and student
        // 2]");
        // }

        /*
         * ______________
         * 
         * int == int
         * double == double
         * 
         * object == object : incorrect :
         * reference compare
         * 
         * object1.equals(object2)
         * 
         * student1.name.equals(student2.name)
         * student1.name==student2.name : incorrect
         * 
         */
    }

}