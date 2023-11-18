#include <stdio.h>


int rev_print(int n) {
	if (!n) return 0;

	int get;
	scanf("%d", &get);
	rev_print(n-1);
	printf("%d\n", get);

	return 0;
}



int main()
{
	int n;
	scanf("%d", &n);
	rev_print(n);
}