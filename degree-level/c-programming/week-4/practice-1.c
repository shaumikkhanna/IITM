#include <stdio.h>


int main() {
	int n;

	scanf("%i", &n);

	int out = 1;
	for (int i = 2; i <= n; ++i) {
		out *= i;
	}

	printf("%i", out);
	return 0;
}