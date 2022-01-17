public class FClass {
	public static void compute(Shape s) {
		s.area();
		s.volume();
	}
	public static void main(String[] args) {
		Rectangle r = new Rectangle();
		Cube c = new Cube();
		compute(r);
		compute(c);
	}
}