public class SavingsAccount extends Account {
	double balance;

	SavingsAccount(SavingsAccount obj) {
		balance = obj.balance;
	}
	SavingsAccount(String pan, double bal) {
		balance = bal;
		PAN = pan;
	}

	public void getBalance() {
		System.out.println(balance);
	}
}