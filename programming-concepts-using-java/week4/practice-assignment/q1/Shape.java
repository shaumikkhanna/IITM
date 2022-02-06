public interface Shape {
	public double area();
	public default double volume() {
		return -1.0;
	}
}