public class Engine {
	private class Fuel {
		String i_fuelType;
		public boolean isFossilFuel(String fuelType) {
			if (fuelType == "Petrol" || fuelType == "Diesel") {
				return true;
			} else {
				return false;
			}
		}
	}
	public String maxMilege(String fuelType) {
		Fuel f = new Fuel();
		if (! f.isFossilFuel(fuelType)) {
			return "Low";
		} else {
			return "High";
		}
	}
}