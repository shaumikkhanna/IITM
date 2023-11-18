#include <stdio.h>


int GCD(int a, int b) {
	int m;
	if (a < b) m = a; else m = b;

	for (int i = m; i > 0; --i)
	{
		if (a%i==0 && b%i==0) {
			return i;
		}
	}
}


int main() 
{
	int a,b;
	scanf("%d",&a);
	scanf("%d",&b);
	printf("%d",GCD(a,b));
	return 0;
}