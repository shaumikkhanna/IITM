public class FClass {
	public static void main(String[] args) {
		int[] arr = {10, 20, 30, 40, 50};
		IntList iList = new IntList(arr);

		Traversable tr1 = iList.getTraversalObj();
		tr1.printForward();
		System.out.println();
		BiTraversable tr2 = iList.getTraversalObj();
		tr2.printBackward();
	}
}