class Point {

    // instance variables
    int x;
    int y;

    // public static final double PIE_VALUE=3.146;

    // constructor
    // it does not return any value not even void
    // constructor name must be equal to classname
    // automatically call -- object creation time

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
        System.out.println("Object Created");
    }

    // methods
    public void display() {
        System.out.println("( " + x + " , " + y + " )");

    }
    // distance method-->

    public double calculateDistance(Point p2) {
        Point p1 = this;

        double xTemp = Math.pow((p1.x - p2.x), 2);
        double yTemp = Math.pow((p1.y - p2.y), 2);
        double xYAdd = xTemp + yTemp;
        double answer = Math.sqrt(xYAdd);
        // System.out.println("Distance " + String.format("%,.2f", answer));
        return answer;

        // this
        // p1 and p2
        // distance cal
        // print
    }

    // midpoint method-->
    public Point calculateMidPoint(Point p2) {

        Point p1 = this;

        int xMid = (p1.x + p2.x) / 2;
        int yMid = (p1.y + p2.y) / 2;

        Point midPint = new Point(xMid, yMid);
        return midPint;

    }

}
