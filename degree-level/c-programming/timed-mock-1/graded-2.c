#include <stdio.h>

int main() {
	int n;
	scanf("%i", &n);
	
	for (int i=2; i <= n; ++i) {
		if (n % i == 0) {
			printf("%i", n/i);
			return 0;
		}
	}
}