public class Manager extends Employee {
	private String department;

	public Manager(int empid_, String name_, String department_) {
		System.out.println("4 ran");
		department = department_;
	}
	public void print() {
		System.out.println("5 ran");
		super.print();
		System.out.println(department);
	}
}