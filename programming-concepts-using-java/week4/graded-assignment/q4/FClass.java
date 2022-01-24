public class FClass {
	public static void main(String[] args) {
		DBIF con = new Database().connectDB("test", "test");
		con.executeStatement("fetch students");
	}
}