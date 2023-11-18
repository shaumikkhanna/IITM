#include <stdio.h>

int main() {
	int x, y, quadrant;
	scanf("%d", &x);
	scanf("%d", &y);

	if (x > 0) {
		if (y > 0) {
			quadrant = 1;
		} else {
			quadrant = 4;
		}
	} else {
		if (y > 0) {
			quadrant = 2;
		} else {
			quadrant = 3;
		}
	}

	printf("Quadrant %d", quadrant);
	return 0;
}