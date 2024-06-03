public class PointExample {
    public static void main(String[] args) {
        Point p1 = new Point(2, 4);
        p1.show();

        Point p2 = new Point(8, 5);
        p2.show();

        p1.calcDistance(p2);

        Point p3 = new Point(56, 21);

        p2.calcDistance(p3);

        var p6 = new Point(10, 20);
        var p7 = new Point(20, 40);
        p6.show();
        p7.show();
        var midPoint = p6.calMidpoint(p7);
        midPoint.show();
    }
}
