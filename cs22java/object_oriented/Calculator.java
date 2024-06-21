public class Calculator {

    void add(int x, int y) {
        System.out.println(x + y);
    }

    void add(int x, int y, int z) {
        System.out.println(x + y + z);
    }

    void add(int x, int y, int z, int a) {
        System.out.println(x + y + z + a);
    }

    void add(int... x) {
        int s = 0;
        for (int h : x) {
            s = s + h;
        }
        System.out.println(s);
    }
}
