// create a class
class PrintNumbers
{
    // create main method
    public static void main(String arr[])
    {
        System.out.println("Printing prime numbers : ");

        // loop from 1 to 100

        /*
         * case 1 :  3
         * 
         * case 2: 4
         * 
         */

        for(int i=1;i<=100;i++)
        {
         
            //check prime
            //agar i prime hai to hame usko print karna hai
            //prime number: 1,i
            // 1 2 3 4 5 6 7   i-1 i 

            //i =4
           
            boolean isPrime=true;
             //isPrime=false
             //i=4
             //j=3
             //2>1
            for(int j=i-1;j>1;j--)
            {
                //j=2,
                // 4%2==0
                //true
                if(i%j==0)
                {
                    isPrime=false;
                    break;
                }
                //j=2
            }

            //isPrime==false
            if(isPrime==true)
            {
                System.out.println(i+"\t");
            }
        }

    }
}