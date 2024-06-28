
class Encap {

    private int age = 56;

    // setters and getters

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        if (age <= 18) {
            System.out.println("Invalid Age ");
            throw new RuntimeException("Invalid Age");
        }
        this.age = age;
    }

}
