#include <stdio.h>


int main() {
	unsigned int a;

	scanf("%08x", &a);
	
	unsigned char* c = (unsigned char*) &a;

	for (int i = 3; i >= 0; --i) {
		printf("%c\n", c[i]);
	}

	return 0;
}