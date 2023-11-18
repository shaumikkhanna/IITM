#include <stdio.h>

int main() {
	float price;
	float total = 0;
	char control = 'y';

	while (control == 'y') {
		scanf("%f", &price);
		total += price;

		scanf(" %c", &control);
	}

	printf("%.2f", total);
	return 0;
}