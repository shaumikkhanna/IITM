public class FClass {
	public static double sum(NumList<? extends Number> iob) {
		double total = 0;
		while (iob.has_next()) {
			total += ((Number)iob.get_next()).doubleValue();
		}
		return total;
	}

	public static void main(String[] args) {
		Integer[] i_arr = {10, 20, 30, 40, 50};
		Double[] d_arr = {1.1, 2.2, 3.3, 4.4, 5.5};

		NumList<Integer> i_list = new NumList<Integer>(i_arr);
		NumList<Double> d_list = new NumList<Double>(d_arr);
		System.out.println(sum(i_list) + " , " + sum(d_list));
	}
}