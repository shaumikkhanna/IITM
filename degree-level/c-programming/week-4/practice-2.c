#include <stdio.h>

int main() {
	int Y;
	int leap = 0;

	scanf("%i", &Y);

	if (Y % 4 == 0) {
		if (Y % 100 != 0) {
			leap = 1;
		} else if (Y % 400 == 0) {
			leap = 1;
		}
	}

	if (leap) {
		printf("%d is a leap year", Y);
	} else {
		printf("%d is not a leap year", Y);
	}

	return 0;
}