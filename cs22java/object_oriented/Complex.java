class Complex {
    // real part of complex number:
    int x;

    // img part of complex number:
    int y;

    // constructor
    Complex(int x, int y) {

        this.x = x;
        this.y = y;
        System.out.println("Complex number created:");
    }

    Complex() {
        this.x = 1;
        this.y = 1;
    }

    void show() {
        System.out.println("( " + x + " + " + y + "i )");
    }

    void show(int x) {
        System.out.println("overloaded how method");
    }

    void show(double x) {
        System.out.println("double overloaded method");
    }

    void show(int x, int y) {
        System.out.println("int int overloaded method");
    }

    int getRealPart() {
        return x;
    }

    int getImagPart() {
        return y;
    }

    Complex add(Complex complex2) {
        Complex complex1 = this;
        int realA = complex1.x + complex2.x;
        int imagA = complex1.y + complex2.y;
        Complex newComplex = new Complex(realA, imagA);
        return newComplex;
    }

    Complex substract(Complex complex2) {
        int realS = this.x - complex2.x;
        int imagS = this.y - complex2.y;

        Complex complexResult = new Complex(realS, imagS);
        return complexResult;
    }
}
