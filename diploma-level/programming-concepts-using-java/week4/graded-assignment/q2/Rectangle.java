public class Rectangle implements Shape, Printable {
	private double w, h;
	public Rectangle(double w_, double h_) {
		this.w = w_;
		this.h = h_;
	}
	public double area() {
		return this.w*this.h;
	}
	public void print() {
		System.out.println(area() + "");
		System.out.println(volume());
	}
}