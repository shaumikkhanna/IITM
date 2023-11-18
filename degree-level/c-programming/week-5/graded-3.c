#include <stdio.h>


int series_sum(int n) {
	int total = 0;
	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= i; ++j) {
			total += j;
		}
	}
	return total;
}


int main()
{
	int n;
	scanf("%d",&n);
	printf("%d", series_sum(n));
	return 0;
}