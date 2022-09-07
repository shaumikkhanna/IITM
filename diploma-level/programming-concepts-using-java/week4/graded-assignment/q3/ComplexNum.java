public class ComplexNum implements NumberType {
	private int r, i;
	public ComplexNum(int r_, int i_) {
		this.r = r_;
		this.i = i_;
	}
	public double norm() {
		return Math.sqrt(r*r + i*i);
	}
}