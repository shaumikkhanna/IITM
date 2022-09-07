public class QClass {
	public static void main(String[] args) {
		Student s = new Student();
		int c = 50;
		int p = 50;
		int m = 50;
		int t = 0;
		
		s.mutateStudent(c, p, m);
		t = s.accessStudent(c, p, m);
		System.out.println(t);
	}
}