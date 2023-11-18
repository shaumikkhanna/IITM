#include <stdio.h>


int greatest(int a, int b, int c) {
	if (a > b) {
		if (c > a) return c;
		else return a;
	} else {
		if (c > b) return c;
		else return b;
	}
}


int main() 
{
	int a, b, c, d;
	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);
	
	d = greatest(a, b, c);
	printf("%d", d);
	
	return 0;
}