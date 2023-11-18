#include <stdio.h>
#include <string.h>


void print_words(char str[], char delim[]) {
	char delimiter = delim[0];

	for (int i = 0; i < strlen(str); i++) {
		if (str[i] == delimiter) {
			printf("\n");
		} else {
			printf("%c", str[i]);
		}
	}
}

int main() 
{
	char str[1000];
	char delim[10];
	// Input a str
	fgets(str,1000,stdin);
	// Input a delimiter
	fgets(delim,10,stdin);

	print_words(str,delim);
	return 0;
}