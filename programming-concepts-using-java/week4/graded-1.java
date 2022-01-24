import java.util.*;

abstract class StringOperations {
	public abstract String reverse(String s);
	public abstract int vowelCount(String s);
}

class StringReverse {
	String reverse(String s) {
		String out = "";
		for (int i = 0; i < s.length(); i++) {
			out = s.charAt(i) + out;
		}
		return out;
	}
}

class UpdatedStrings extends StringReverse{

	static boolean isVowel(char c) {
		c = Character.toLowerCase(c);
		return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
	}
	int vowelCount(String s) {
		int out = 0;
		for (int i = 0; i < s.length(); i++) {
			if (UpdatedStrings.isVowel(s.charAt(i))) {
				out++;
			}
		}
		return out;
	}
}

class Example {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.next();
		UpdatedStrings str = new UpdatedStrings();
		System.out.println("Reverse of "+ s + " is "+ str.reverse(s));
		System.out.println("Vowel count of "+ s + " is "+ str.vowelCount(s));
	}
}