#include <stdio.h>

int main() {
	int a, b, c;
	scanf("%i", &a);
	scanf("%i", &b);
	scanf("%i", &c);
	
	if (a==b && b==c) {
		printf("Equilateral");
	} else if (a!=b && b!=c && c!=a) {
		printf("Scalene");
	} else {
		printf("Isosceles");
	}
}