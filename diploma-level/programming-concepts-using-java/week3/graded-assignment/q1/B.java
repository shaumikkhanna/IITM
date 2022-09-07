public class B extends A {
	public void display(String s) {
		display();
		System.out.println(s);
	}
	public static void main(String[] args) {
		A a = new B();
		((B) a).display("Ram");
	}
}