public class FClass {
	public static void main(String[] args) {
		Developer[] dA = {new Developer("A", 50000.0), new Developer("B", 40000.0), new Developer("C", 45000.0)};
		Manager[] mA = {new Manager("X", 65000.0), new Manager("Y", 51000.0)};
		
		SalaryStat<Developer> dO = new SalaryStat<Developer>(dA);
		SalaryStat<Manager> mO = new SalaryStat<Manager>(mA);

		if (mO.greaterSalary(dO)){
			System.out.println("managers have higher salary expenditure");
		} else {
			System.out.println("developers have higher salary expenditure");
		}
	}
}