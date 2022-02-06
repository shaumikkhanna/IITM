public class Student {
	private int rollno;
	private int chemMarks;
	private int phyMarks;
	private int mathsMarks;

	public int accessStudent(int c, int p, int m) {
		return c + p + m;
	}
	public void mutateStudent(int c, int p, int m) {
		chemMarks = c;
		phyMarks = p;
		mathsMarks = m;
	}
}