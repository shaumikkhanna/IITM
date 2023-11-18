#include <stdio.h>


int isPrime(int p) {
	if (p == 1) return 0;

	for (int i = 2; i < p; ++i) {
		if (p % i == 0) {
			return 0;
		}
	}
	return 1;
}


int prime_sum(int p, int q) {
	int total = 0;

	for (int i = p; i <= q; ++i) {
		if (isPrime(i)) {
			printf("%d ", i);
			total += i;
		}
	}
	return total;
}



int main() 
{
	int p,q;
	scanf("%d",&p);
	scanf("%d",&q);
	printf("%d",prime_sum(p,q));
	return 0;
}