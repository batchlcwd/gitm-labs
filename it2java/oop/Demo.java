public class Demo {
    public static void main(String[] args) {
        System.out.println("Program started");

        int x = 40;
        // creating object
        Student student1 = new Student(
                3435,
                "Ashish",
                "GITM");
        // student1.name = "Ashish";
        // student1.college = "GITM";
        // student1.rollNumber = 1241;
        student1.show();

        Student student2 = new Student(123, "Ram Singh", "BBD");
        // student2.name = "RAM SINGH";
        // student2.college = "BBD";
        // student2.rollNumber = 2324;

        student2.show();

    }
}
