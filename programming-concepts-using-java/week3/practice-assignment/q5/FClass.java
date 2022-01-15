public class FClass {
	public static void main(String[] args) {
		new Parent().f1(); /* From parent class */
		new Child().f1(); /* From child class */
		((Parent) new Child()).f1(); /* From child class */
	}
}