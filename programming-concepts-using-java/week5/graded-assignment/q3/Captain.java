public class Captain extends Player {
	public Captain(String name, String type) {
		super(name, type);
	}
	public String toString() {
		return "Player [name=" + this.getName() + ",type=" + this.getType() + "]";
	}
}