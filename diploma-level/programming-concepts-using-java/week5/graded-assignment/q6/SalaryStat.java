public class SalaryStat<T extends Employee> {
	private T[] eps;

	public SalaryStat(T[] eps) {
		this.eps = eps;
	}

	private double getTotalSalary() {
		double total = 0;
		for (int i = 0; i < eps.length; i++) {
			total += eps[i].getSalary();
		}
		return total;
	}
	public boolean greaterSalary(SalaryStat<? extends Employee> d) {
		return (this.getTotalSalary() > d.getTotalSalary());
	}
}