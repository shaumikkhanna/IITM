public class FClass {
	public static void main(String[] args) {
		TreeSet<String> empList = new TreeSet<String>();
		empList.add(new Employee("raj", 30000.00));
		empList.add(new Employee("akash", 60000.00));
		empList.add(new Employee("biraj", 60000.00));
		empList.add(new Employee("vinay", 40000.00));
		for (Employee e: empList) {
			System.out.println(e);
		}
	}
}