public class Capacity {
	public <T extends Vehicle> void seating(T obj) {
		obj.capacity();
	}
	public static void main(String[] args) {
		Capacity bike = new Capacity();
		bike.seating(new Bike());
		Capacity auto = new Capacity();
		auto.seating(new Auto());
	}
}