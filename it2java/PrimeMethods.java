import java.util.Scanner;

class PrimeMethods
{

    static boolean isPrime(int n)
    {
        //logic prime
        boolean check=true ;
        for(int i=n-1;i>=2;i--)
        {
            if(n%i==0)
            {
                check=false;
                break;
            }
        }

        return check;
    }

    public static void main(String[] args) {

        Scanner sc=new Scanner(System.in);
        System.out.println("Enter range : [n....m]");
        int lr=sc.nextInt();
        int ur=sc.nextInt();

        for(int i=lr;i<=ur;i++)
        {
            boolean result=isPrime(i);
            if(result)
            {
                System.out.println(i);
            }
        }
        


    }
}