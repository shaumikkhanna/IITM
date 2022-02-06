public class Example {
	public static void main(String[] args) {
		Engine e = new Engine();
		int i = 0;
		String[] fType = {"Biodiesel", "Diesel", "Petrol", "Steam"};
		for (i = 0; i < 4; i++) {
			System.out.println(e.maxMilege(fType[i]));
		}
	}
}