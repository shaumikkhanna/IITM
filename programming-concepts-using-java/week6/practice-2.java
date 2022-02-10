import java.util.*;


abstract class Account implements Comparable<Account> {
	String acc_no;
	double balance;	
	
	public Account(String no,double bal) {
		this.acc_no = no; 
		this.balance = bal;
	}	
	//Override "compareTo" method here
	public int compareTo(Account other) {
		if (this.balance > other.balance) {
			return -1;
		} else if (this.balance < other.balance) {
			return 1;
		} else {
			return 0;
		}
	}
	// Override "equals" method here
	public boolean equals(Object o) {
		Account other = (Account) o;
		return this.acc_no.equals(other.acc_no);
	}
	// Override "hashCode" method here
	public int hashCode() {
		return 69;
	}
}

class SavingsAccount extends Account {
	public SavingsAccount(String acc_no, double bal) {
		super(acc_no, bal);
	}
	// Override the toString() method
	public String toString() {
		return "Savings Account:" + this.acc_no + " , Balance:" + this.balance;
	}
}


class CurrentAccount extends Account {
	double overdraft_limit;

	public CurrentAccount(String acc_no, double bal, double odl) {
		super(acc_no, bal);
		this.overdraft_limit = odl;
	}

	// Override the toString() method}}
	public String toString() {
		return "Current Account:" + this.acc_no + " , Balance:" + this.balance;
	}
}

public class Test4 {
	 // Define the `accountProcessor' method here
	public static void accountProcessor(ArrayList<Account> arr) {
		LinkedHashSet<Account> lhs = new LinkedHashSet<Account>(arr);
		TreeSet<Account> ts = new TreeSet<Account>(lhs);
		Iterator<Account> iter = ts.iterator();
		while (iter.hasNext()) {
			System.out.println(iter.next());
		}
	}

	public static void main(String args[]) {
		Scanner s = new Scanner(System.in);
		ArrayList<Account> acc = new ArrayList<Account>();
		
		//reading the number of savings accounts
		int s_acc_count = s.nextInt();
		for (int i = 1; i <= s_acc_count; i++) {
			//reading acc no
			String no = s.next();
			//reading balance
			double bal = s.nextDouble();
			acc.add(new SavingsAccount(no,bal));
		}
		
		//reading the number of current accounts
		int c_acc_count = s.nextInt();
		for (int i=1; i <= c_acc_count; i++) {
			//reading acc no
			String no = s.next();
			//reading balance
			double bal = s.nextDouble();
			//reading overdraft limit
			double lim = s.nextDouble();
			acc.add(new CurrentAccount(no,bal,lim));
		}
		
		accountProcessor(acc);
	}
}