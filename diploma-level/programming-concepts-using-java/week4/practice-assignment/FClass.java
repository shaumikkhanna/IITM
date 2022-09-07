public class FClass {
	public static void sort(Comparable[] names) {
		// Bubble sort
		for (int i = 0; i < names.length; i++) {
			for (int j = 0; j < names.length; j++) {
				if ( names[j].comp(names[j+1]) > 0 ) {
					// Swap names[j] and names[j+1]
					Comparable tname = names[j];
					names[j] = names[j+1];
					names[j+1] = tname;
				}
			}
		}
	}
	public static void main(String[] args) {
		Name[] names = new Name[] {new Name("Charlotte", "Brown"),
									new Name("Ava", "Smith"),
									new Name("Emma Williams")
									new Name("Olivia", "Smith")
									new Name("Emma", "Johnson")}
		sort(names);
		for (int i = 0; i < names.length; i++) {
			names[i].print();
		}
	}
}