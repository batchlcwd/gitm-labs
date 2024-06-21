class ComplexExample {
    public static void main(String[] args) {

        // working space:
        // WAP to sum two complex number:
        // (8+6j)
        // (7+8j)
        // (15+14j)
        // two int
        // real r1= (4+5j);

        Complex c1 = new Complex(8, 6);
        c1.show();
        // int real = c1.getRealPart();
        // System.out.println(real);

        // int imag = c1.getImagPart();
        // System.out.println(imag);

        Complex c2 = new Complex(4, 10);
        c2.show();

        Complex result = c1.add(c2);
        result.show();

        Complex subsResult = c1.substract(c2);
        subsResult.show();

        Complex answer = subsResult.add(result);
        answer.show();

    }

    // HOME WORK:
    // WAP to multiply and divide two complex number.
}
