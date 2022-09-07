public class Account {
	String PAN;
	String IFSC;
	
	Account(Account obj) {
		PAN = obj.PAN;
		IFSC = obj.IFSC;
	}
	public void getPan() {
		System.out.println(PAN);
	}
}