#include <stdio.h>


int main() {
	int a, b;

	scanf("%d", &a);
	scanf("%d", &b);

	int min = (a < b)? a: b;

	for (int i = 2; i <= min; ++i) {
		if (a % i == 0 && b % i == 0) {
			printf("Not Coprime");
			return 0;
		}
	}
	printf("Coprime");
	return 0;
}