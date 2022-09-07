import java.util.*;


class RemoveStudent{
	public boolean property(Double value) {
		if (value < 65) {
			return true;
		}
		return false;				
	}
	public void detained(Map<String, Double> obj) {
		// Define the detained() method}}
		ArrayList<String> keys_to_remove = new ArrayList<String>();
		for (Map.Entry<String, Double> e : obj.entrySet()) {
			String k = e.getKey();
			Double v = e.getValue();
			if (this.property(v)) {
				keys_to_remove.add(k);
			}
		}
		for (String k : keys_to_remove) {
			obj.remove(k);
		}
		this.display(obj);
	}
	public void display(Map<String, Double> obj) {
			System.out.println(obj);
	}
}

public class Test {
	public static void main(String[] args) {
		Map<String,Double> map = new TreeMap<String,Double>();
		Scanner scanner = new Scanner(System.in); 
		for (int i = 0; i < 6; i++) {
			map.put(scanner.next(),scanner.nextDouble());
		}
		RemoveStudent obj = new RemoveStudent();
		obj.detained(map);
	}
}