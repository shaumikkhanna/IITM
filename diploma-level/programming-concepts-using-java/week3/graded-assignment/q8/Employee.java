public class Employee {
	private int empid;
	private String name;

	public Employee(int empid_, String name_) {
		empid = empid_;
		name = name_;
	}
	public Employee() {
		this(0, "unknown");
	}
	public void print() {
		System.out.print(empid + ":" + name + ":");
	}
}