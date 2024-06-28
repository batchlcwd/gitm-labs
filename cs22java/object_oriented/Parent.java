class Parent {

    int x = 600;

    public void showX() {
        System.out.println("Showing parent class variables");
        System.out.println("x = " + x);
    }
}

class Child extends Parent {
    int y = 900;
}