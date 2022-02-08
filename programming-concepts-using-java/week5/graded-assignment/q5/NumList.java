public class NumList<T extends Number> implements Iterator {
	private T[] list;
	private int idx;

	public NumList(T[] list) {
		this.list = list;
		this.idx = 0;
	}

	public boolean has_next(){
		return this.idx < list.length - 1;
	}
	public Object get_next(){
		this.idx++;
		return list[idx];
	}
}