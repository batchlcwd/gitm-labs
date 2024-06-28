class PointExample {
    public static void main(String[] args) {
        // 1st approch
        // int x1=45;
        // int y1=34;

        // int x2=45;
        // int y2=45;

        // 100

        // 2 approch
        // Data types--> class
        int x = 45;
        Point p1 = new Point(45, 34);
        // p1.x = 45;
        // p1.y = 34;
        p1.display();

        Point p2 = new Point(33, 11);
        // p2.x = 33;
        // p2.y = 11;

        p2.display();

        Point p3 = new Point(2, 4);
        Point p4 = new Point(20, 4);
        Point p5 = new Point(200, 4);
        Point p6 = new Point(2000, 4);
        Point p7 = new Point(21, 4);
        Point p8 = new Point(223, 4);
        p3.display();
        p4.display();
        p5.display();
        p6.display();
        p7.display();
        p8.display();

        double dis = p1.calculateDistance(p2);
        System.out.println("Distance : " + dis);

        // p6.calculateDistance(p7);

        double dis2 = p4.calculateDistance(p5);
        System.out.println("Distance " + dis2);

        Point p100 = new Point(10, 20);
        Point p101 = new Point(5, 10);

        p100.display();
        p101.display();
        Point midPoint = p100.calculateMidPoint(p101);
        midPoint.display();

        Point mPoint2 = midPoint.calculateMidPoint(p101);
        mPoint2.display();

    }
}