public class NumData {
	private Number n;

	public NumData(Number n) {
		this.n = n;
	}

	public String getMetaInfo() {
		if (this.n instanceof Integer) {
			return "Integer type, value = " + this.n;
		} else if (this.n instanceof Double) {
			return "Double type, value = " + this.n;
		} else if (this.n instanceof Character) {
			return "Character type, value = " + this.n;
		} else {
			return "Number type, value = " + this.n;
		}
	}
}