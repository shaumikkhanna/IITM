#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>


char* repeat_string(char* str, int n) {
	char* out = (char*) malloc(n * strlen(str) * sizeof(char));
	for (int i = 0; i < n; i++) {
		strcpy(out+i*strlen(str), str);
	}
	return out;
}


int main()
{
	char str[10];
	int n;
	scanf("%s",str);
	scanf("%d",&n);
	char* repeated_string = repeat_string(str, n);
	printf("%s",repeated_string);
	free(repeated_string);
}
