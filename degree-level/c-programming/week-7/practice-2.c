#include <stdio.h>
#include <string.h>


int main() {
	char mystring[100];
	scanf("%s", mystring);

	int n = strlen(mystring);

	for (int i = 0; i < n / 2; ++i) {
		if (mystring[i] != mystring[n-1-i]) {
			printf("Not Palindrome");
			return 0;
		}
	}

	printf("Palindrome");
	return 0;
}