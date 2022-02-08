public class Player {
	private String name;
	private String type;

	public Player(String name, String type) {
		this.name = name;
		this.type = type;
	}
	public String getName() {
		return this.name;
	}
	public String getType() {
		return this.type;
	}
	public String toString() {
		return "Player [name=" + this.name + ",type=" + this.type + "]";
	}
}