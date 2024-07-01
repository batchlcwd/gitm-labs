package inheritance;

public class Calc {

    //constructor overload

    public Calc(){
        System.out.println("Default constructor");
    }

    public Calc(int a){
        System.out.println("Constructor with int type argument");
    }

    public Calc(double d){
        System.out.println("constructor with double argument");
    }

    public void add(int a,int b){
        System.out.println(a+b);
    }

    public void add(int a, int b, int c)
    {
        System.out.println(a+b+c);
    }


}
