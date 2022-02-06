public class IntList extends List {
	private final int N = 5;
	private int[] iArr;

	public IntList(int[] arr) {
		iArr = arr;
	}

	public void add(Object elem) {
		// Adds object elem to iArr
	}
	Traversal getTraversalObj() {
		return new Traversal();
	}

	private class Traversal implements BiTraversable {
		public void printForward() {
			for (int i = 0; i < N; i++) {
				System.out.print(iArr[i] + " ");
			}
		}
		public void printBackward() {
			for (int i = 0; i < N; i++) {
				System.out.print(iArr[N-1-i] + " ");
			}
		}
	}
}