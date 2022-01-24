public interface Animal {
	void sound();
	default void eat(String animal) {
		System.out.println(animal + " eats every day");
	}
}