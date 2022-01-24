public class Database {
	private ConnectionObj cobj = null;

	public DBIF connectDB(String u, String p) {
		if (isValidate(u, p)) {
			cobj = new ConnectionObj();
		}
		return cobj;
	}
	public boolean isValidate(String u, String p) {
		return true;
	}
	private class ConnectionObj implements DBIF {
		public void executeStatement(String qry) {
			System.out.println("Exectute : " + qry);
		}
	}
}