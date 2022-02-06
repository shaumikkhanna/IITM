public interface Flyable {
	public void fly();
	public default void travel() {
		System.out.println("Travel with wings");
	}
}