public class Mammal {
	public String name;
	public int lifespan;

	public Mammal() {
		this.name = "Tiger";
		this.lifespan = 45;
	}

	public void show() {
		System.out.format("name = %s : lifespan = %d", this.name, this.lifespan);
	}
	public void display() {
		System.out.println("Mammal details");
	}
}