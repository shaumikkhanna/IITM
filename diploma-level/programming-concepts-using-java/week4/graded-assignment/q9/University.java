public class University {
	public int univ_id;

	private class College {
		private String college_name;

		public void getName() {
			System.out.println(college_name);
		}
		public College(String name) {
			college_name = name;
		}
	}

	public College getReference() {
		return new College("IITM");
	}
}