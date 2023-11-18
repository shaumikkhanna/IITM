#include <stdio.h>
#include <string.h>


void title_case(char s[]) {
	int len = strlen(s);
	int first_letter = 1;
	char c;

	for (int i = 0; i < len; ++i) {
		c = s[i];

		if (97 <= c && c <= 122) {
			if (first_letter) {
				printf("%c", c-32);
				first_letter = 0;
			} else {
				printf("%c", c);
			}
		} else if (65 <= c && c <= 90) {
			if (first_letter) {
				printf("%c", c);
				first_letter = 0;
			} else {
				printf("%c", c+32);
			}
		} else if (c == 32) {
			first_letter = 1;
			printf("%c", c);
		} else {
			first_letter = 0;
			printf("%c", c);
		}
	}
}


int main() {
    char sentence[1000];

    // It is safe to use fgets if your input is a string of spaces.
    fgets(sentence,1000,stdin);
    title_case(sentence);
    return 0;
}