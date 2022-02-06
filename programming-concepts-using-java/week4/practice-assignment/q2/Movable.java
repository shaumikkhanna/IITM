public interface Movable {
	public void move();
	public default void travel() {
		System.out.println("Travel with legs");
	}
}