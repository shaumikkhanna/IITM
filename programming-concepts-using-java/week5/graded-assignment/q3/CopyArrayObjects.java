public class CopyArrayObjects {
	public static <S extends T, T> void copy(S[] src, T[] tgt) {
		int limit = Math.min(src.length, tgt.length);
		for (int i = 0; i < limit; i++) {
			tgt[i] = src[i];
		}
	}
}