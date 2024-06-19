import java.util.Scanner;

public class DynamicPointOperations {
    public static void main(String[] args) {
        // do points lene hai.

        /// dyamic:
        Scanner sc = new Scanner(System.in);
        // point1:
        System.out.println("Enter x1:");
        int x1 = sc.nextInt();

        System.out.println("Enter y1: ");
        int y1 = sc.nextInt();

        Point p1 = new Point(x1, y1, "Point1");

        System.out.println("Enter x2:");
        int x2 = sc.nextInt();

        System.out.println("Enter y2:");
        int y2 = sc.nextInt();

        Point p2 = new Point(x2, y2, "Point2");

        double result11 = p1.calculateDistance(p2);
        System.out.println("Distance " + result11);

        Point midPoint = p1.findMidPoint(p2);
        midPoint.show();
    }
}
