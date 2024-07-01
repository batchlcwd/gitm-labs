package inheritance;

import java.io.FileNotFoundException;

public class Human extends Animal {

    //override

    RuntimeException eat() {
        System.out.println("Human is eating");
        return null;
    }
}
