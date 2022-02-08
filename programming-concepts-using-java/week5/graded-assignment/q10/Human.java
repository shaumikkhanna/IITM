public class Human implements Walkable {
	double pace_length = 0.85;
	public void showPaceLength() {
		System.out.format("Average pace length : %f meters", pace_length);
	}
}