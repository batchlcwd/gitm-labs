public class Point {
    // instance variables
    int x, y;

    // Constructor:
    Point(int x, int y) {
        // local to constructor
        this.x = x;
        this.y = y;
        System.out.println("Point Created");
    }

    void show() {
        // ( 5, 7 )
        System.out.println("( " + x + " , " + y + " )");

    }

    void calcDistance(Point p2) {
        // p1 and p2
        // this -> current invoking
        double d = Math.pow((p2.x - this.x), 2) + Math.pow(p2.y - this.y, 2);

        double answer = Math.sqrt(d);
        System.out.println(
                "Distance between ( " + this.x + "," + this.y + " ) and ( " + p2.x + " ," + p2.y + " ) is: " + answer);

    }

    Point calMidpoint(Point p2) {
        // this and p2

        int midX = (this.x + p2.x) / 2;
        int midY = (this.y + p2.y) / 2;
        Point midPoint = new Point(midX, midY);
        return midPoint;

    }

}
