public class Student {
	public String sname;
	public String sid;
	public int sclass;

	public Student(String s_name, String s_id, int s_class) {
		sname = s_name;
		sid = s_id;
		sclass = s_class;
	}
	// public Student() {
	// 	sname = "john doe";
	// 	sid = "A";
	// 	sclass = 12;
	// }
	public void display() {
		System.out.println("name : " + this.sname);
		System.out.println("id : " + this.sid);
		System.out.println("class : " + this.sclass);
	}
}