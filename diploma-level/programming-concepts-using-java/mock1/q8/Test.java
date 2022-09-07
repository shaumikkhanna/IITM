public class Test {
	public static void main(String[] args) {
		SavingsAccount acc1 = new SavingsAccount("CLX234", 1024.22);
		Account acc2 = new SavingsAccount(acc1);
		acc2.getBalance();
		acc2.getPan();
	}
}