#include <stdio.h>


int main() {
	unsigned int a;

	scanf("%08x", &a);

	printf("%u\n", a);
	printf("%d\n", (int) a);
}