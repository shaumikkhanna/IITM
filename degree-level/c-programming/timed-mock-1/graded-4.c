#include <stdio.h>

int main() {
	int a, b;
	int out = 0;
	scanf("%i", &a);
	scanf("%i", &b);
	
	for (int i = a; i <= b; ++i)
	{
		if ((i % 3 == 0 || i % 5 == 0) && i % 15 != 0) {
			out++;
		}
	}
	printf("%i", out);
	return 0;
	
}