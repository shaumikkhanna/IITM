public class Test {
	public static void main(String[] args) {
		String[] buffer = {"Item 0"};
		Restaurant obj = new Restaurant(buffer);
		Restaurant.Producer p = obj.new Producer();
		p.produce();
	}
}