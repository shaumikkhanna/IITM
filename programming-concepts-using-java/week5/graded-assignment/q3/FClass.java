public class FClass {
	public static void main(String[] args) {
		Captain captain1 = new Captain("Virat", "Batting");
		Captain captain2 = new Captain("Hardik", "All Rounder");
		Captain captain3 = new Captain("Jasprit", "Bowling");
		Captain[] captain = {captain1, captain2, captain3};

		Player[] player = new Captain[2];
		CopyArrayObjects.copy(captain,player);

		for (Player p : player) {
			System.out.println("" + p);
		}
	}
}