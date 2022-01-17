public class Manager extends Employee {
	private String department;

	public Manager(int empid_, String name_, String department_) {
		super(empid_, name_);
		department = department_;
	}
	public void print() {
		super.print();
		System.out.println(department);
	}
}