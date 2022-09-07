public class Rectangle implements Shape, Printable {
	private double w;
	private double h;

	public Rectangle(double w_, double h_) {
		w = w_;
		h = h_;
	}

	public double area() {
		return w*h;
	}
	public void print() {
		System.out.print(area() + " ");
		System.out.print(volume());
	}
}