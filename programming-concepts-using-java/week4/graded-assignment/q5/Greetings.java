public class Greetings {
	private String country;

	public void setCountry(String s) {
		this.country = s;
	}
	public String getCountry() {
		return this.country;
	}
	public Inter checkCountry() {
		if (getCountry() == "India") {
			return new IndiaGreetings();
		}
		return new WorldGreetings();
	}
	private class IndiaGreetings implements Inter {
		public void greet() {
			System.out.println("Hello India");
		}
	}
	private class WorldGreetings implements Inter {
		public void greet() {
			System.out.println("Hello World");
		}
	}
}	