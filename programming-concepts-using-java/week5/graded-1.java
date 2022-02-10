import java.util.*;

class ComplexNum<T extends Number> {
	private T real;
	private T imag;

	public ComplexNum(T real, T imag) {
		this.real = real;
		this.imag = imag;
	}

	public String toString() {
		return this.real + " + " + this.imag + "i";
	}
	public ComplexNum<Double> add(ComplexNum other) {
		double new_real = this.real.doubleValue() + other.real.doubleValue();
		double new_imag = this.imag.doubleValue() + other.imag.doubleValue();
		return new ComplexNum<Double>(new_real, new_imag);
	}
}

public class Main{
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1, n2;
        double d1, d2;
        n1 = sc.nextInt();
        n2 = sc.nextInt();
        d1 = sc.nextDouble();
        d2 = sc.nextDouble();
        ComplexNum<Integer> c1 = new ComplexNum<Integer>(n1, n2);
        ComplexNum<Double> c2 = new ComplexNum<Double>(d1, d2);
    	System.out.println(c1.getClass().getName());
    	System.out.println(c2.getClass().getName());
        ComplexNum<Double> c3 = c1.add(c2);
    	System.out.println(c3.getClass().getName());
        System.out.println(c1 + " + " + c2 + " = " + c3);
    }
}