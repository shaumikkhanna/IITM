public class Mammal<T> {
	public String name;
	public T group;

	public Mammal(T obj) {
		name = obj.getClass().getSimpleName();
		group = obj;
	}
	public void print() {
		System.out.println(name);
		group.showPaceLength();
	}
}