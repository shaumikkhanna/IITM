#include <stdio.h>

int main() {
	int n, cookies;
	int total = 0;

	scanf("%i", &n);

	for (int i = 0; i < n; ++i)
	{
		scanf("%i", &cookies);
		total += cookies;
	}

	printf("%i", total);
	return 0;
}