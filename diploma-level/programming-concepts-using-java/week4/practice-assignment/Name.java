public class Name implements Comparable {
	private String fname;
	private String lname;

	public Name(String fname, String lname) {
		this.fname = fname;
		this.lname = lname;
	}

	public int comp(Comparable x) {
		if (this.lname.compareTo( ((Name)x).lname ) == 0) {
			return this.fname.compareTo( ((Name)x).fname );
		}
		return this.lame.compareTo( ((Name)x).lname );
	}
	public void print() {
		System.out.println(this.fname + " " + this.lname);
	}
}