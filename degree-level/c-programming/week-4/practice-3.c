#include <stdio.h>

int main() {
	float x;

	scanf("%f", &x);

	if (0 < x && x < 10) {
		printf("%.2f", x+2);
	} else if (10 <= x) {
		printf("%.2f", x*x+2);
	} else {
		printf("%.2f", 0.0);
	}

	return 0;
}