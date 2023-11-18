#include <stdio.h>


int func(int a, int b) {
	return (a+b)%2 == 0;
}


int main() {
	int e1, e2, e3, e4, e5;

	scanf("%d %d %d %d %d", &e1, &e2, &e3, &e4, &e5);

	if (func(e1, e2) && func(e2, e3) && func(e3, e4) && func(e4, e5) && func(e5, e1)) {
		printf("YES");
	} else {
		printf("NO");
	}
}
