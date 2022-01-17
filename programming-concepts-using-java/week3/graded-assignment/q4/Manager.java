public class Manager extends Employee, TeamLead {
	public void display() {
		System.out.println("In Manager Class");
	}
	public static void main(String[] args) {
		TeamLead t = new Employee();
	}
}