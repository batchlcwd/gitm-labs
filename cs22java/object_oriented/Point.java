
public class Point {

    int x, y;
    // int z
    // point name
    String name;

    // constructor:
    // method/function
    // name == classname
    // does not return any value: not even void
    Point(int x, int y, String name) {
        // code yaha likhnege
        // x aur y ki value initilise
        // this keyword
        this.x = x;
        this.y = y;
        this.name = name;
        System.out.println("Object Create with " + this.name);

    }

    // sare properties ko dikha de:
    // method
    void show() {
        // kam : kiska kam
        System.out.println(" " + this.name + " ( " + this.x + "," + this.y + " )");
    }

    // jo distance calculate
    double calculateDistance(Point point2) {
        // asan :
        // requirement
        // point1==? p10==(this)
        // point2= poin2

        double d1 = Math.pow((this.x - point2.x), 2) + Math.pow((this.y - point2.y), 2);
        double answer = Math.sqrt(d1);
        // System.out.println("distance: " + answer);
        return answer;
    }

    Point findMidPoint(Point point2) {
        // this
        // point2

        int midX = (this.x + point2.x) / 2;
        int midY = (this.y + point2.y) / 2;
        Point midPoint = new Point(midX, midY,
                "MidPoint");
        return midPoint;
    }

}
