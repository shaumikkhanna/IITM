public class FClass {
	public static void dolt(Bird b) {
		b.fly();
		if (b instanceof Duck) {
			((Duck) b.swim();
		}
	}
	public static void main(String[] args) {
		Duck d = new Duck();
		dolt(d);
	}
}