public class FClass {
	public static void main(String[] args) {
		A obj = new B(2.718);

		A ptr1 = (A) obj;
		A ptr2 = (B) obj;
		B ptr3 = (B) obj;

		ptr1.show();
		ptr2.show();
		ptr3.show();
	}
}

// e = 2.718
// e = 2.718
// e = 2.718
