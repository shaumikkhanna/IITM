public class Toppers extends Student {
	public int marks;

	public Toppers(int marks) {
		this.marks = marks;
	}
	public void display() {
		super.display();
		System.out.println("marks : " + this.marks);
	}
}