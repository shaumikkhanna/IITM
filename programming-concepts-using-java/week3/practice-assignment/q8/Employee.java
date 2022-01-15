public class Employee {
	private int empid;
	private String name;

	public Employee(int empid_, String name_) {
		System.out.println("1 ran");
		empid = empid_;
		name = name_;
	}
	public Employee() {
		this(0, "unknown");
		System.out.println("2 ran");
	}
	public void print() {
		System.out.println("3 ran");
		System.out.print(empid + ":" + name + ":");
	}
}