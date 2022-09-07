public class FClass {
	public static void main(String[] args) {
		Integer iO = 10;
		Float fO = 3.14f;
		Character cO = 'A';

		NumData o1 = new NumData(iO);
		NumData o2 = new NumData(fO);
		NumData o3 = new NumData(cO);
		
		System.out.println(o1.getMetaInfo());
		System.out.println(o2.getMetaInfo());
		System.out.println(o3.getMetaInfo());
	}
}