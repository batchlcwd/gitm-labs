import java.util.Scanner;

class DistanceFinder {
    public static void main(String[] args) {
        System.out.println("Going to find distance");

        Scanner sc = new Scanner(System.in);

        // input the data:

        Point p1 = new Point(5, 4, "point1");
        Point p2 = new Point(10, 20, "point2");
        p1.show();
        p2.show();

        double result = p1.calculateDistance(p2);
        System.out.println("Distance " + result);
        Point midPoint = p1.findMidPoint(p2);
        midPoint.show();
        // System.out.println(midPoint.name);

    }
}