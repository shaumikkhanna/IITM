public class Example2 extends Example1 {
	public int i = 20;
	public void display() {
		System.out.println("In child class");
	}
	public static void main(String[] args) {
		Example1 obj = new Example2();
		obj.display(); /* In child class */
		System.out.println(obj.i); /* 10 */
	}
}
