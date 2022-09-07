import java.util.*;

class CricketPlayer {
	private String name;
	private int wickets;
	private int runs;
	private int matches;

	public CricketPlayer(String s, int w, int r, int m) {
		this.name = s;
		this.wickets = w;
		this.runs = r;
		this.matches = m;
	}

	public String getName() {
		return name;
	}
	public int getWickets() {
		return wickets;
	}
	public int getRuns() {
		return runs;
	}
	public double avgRuns() {
		return runs/matches;
	}
	public double avgWickets() {
		return wickets/matches;
	}
}

	public class Main {
		// Define displayPlayers() method here
		public static void displayPlayers(ArrayList<CricketPlayer> bw, ArrayList<CricketPlayer> bt) {
			for (CricketPlayer p : bw) {
				System.out.print(p.getName() + " ");
			}
			System.out.println();
			for (CricketPlayer p : bt) {
				System.out.print(p.getName() + " ");
			}
		}

		public static void main(String[] args) {
			Scanner sc = new Scanner(System.in);
			CricketPlayer p1 = new CricketPlayer(sc.next(), sc.nextInt(), sc.nextInt(), sc.nextInt());
			CricketPlayer p2 = new CricketPlayer(sc.next(), sc.nextInt(), sc.nextInt(), sc.nextInt());
			CricketPlayer p3 = new CricketPlayer(sc.next(), sc.nextInt(), sc.nextInt(), sc.nextInt());
			CricketPlayer p4 = new CricketPlayer(sc.next(), sc.nextInt(), sc.nextInt(), sc.nextInt());

			// Define ArrayList objects here
			ArrayList<CricketPlayer> bw = new ArrayList<CricketPlayer>();
			ArrayList<CricketPlayer> bt = new ArrayList<CricketPlayer>();
			
			ArrayList<CricketPlayer> players = new ArrayList<CricketPlayer>();
			players.add(p1);
			players.add(p2);
			players.add(p3);
			players.add(p4);

			for (CricketPlayer p : players) {
				if (p.avgRuns() > 25) {
					bt.add(p);
				}
				if (p.avgWickets() > 1) {
					bw.add(p);
				}
			}

			displayPlayers(bw, bt);
	}
}  