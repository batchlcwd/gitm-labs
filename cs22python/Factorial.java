import java.math.BigInteger;
import java.util.Scanner;

class Factorial{
    public static void main(String[] args){

        Scanner ob=new Scanner(System.in);
        System.out.println("Enter your number");
        BigInteger n=ob.nextBigInteger();
        
        BigInteger f=new BigInteger("1");
        for(long i=n.longValue();i>=1;i--){
            f=f.multiply(new BigInteger(i+""));
        }
        System.out.println("Factorial "+f.toString());

    }
}