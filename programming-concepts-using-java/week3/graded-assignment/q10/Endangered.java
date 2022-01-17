public class Endangered extends Mammal {
	public boolean endanger_status;

	public Endangered() {
		endanger_status = false;
	}

	public void show() {
		System.out.println("endanger status of " + this.name + " is " + this.endanger_status);
	}
	public void display(String species) {
		System.out.println("Endanger status");
	}
}