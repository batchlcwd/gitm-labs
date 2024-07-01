package inheritance;

public class Demo {
    public static void main(String[] args) {
        System.out.println("this is demo class");
//        Calc calc = new Calc(4.6);
//        calc.add(2, 3);
//        calc.add(1, 1, 1);
        Human human = new Human();
        human.eat();
        human.sleep();
        Cat cat = new Cat();
        cat.eat();
        human.sleep();

    }
}
