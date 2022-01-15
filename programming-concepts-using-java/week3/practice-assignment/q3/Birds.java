public class Birds extends Animals {
	public void swim() { /* Error: Overridden Method is final */
		System.out.println("Birds swim");
	}
	public void communicate() { /* Error: Overrideen Method is static */
		System.out.println("Birds communicate");
	}
	public void fly() {
		System.out.println("Birds fly");
	}
}