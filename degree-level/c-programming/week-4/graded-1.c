#include <stdio.h>

int main()
{
	float amt;
	float final;

	scanf("%f", &amt);

	if (amt < 200) {
		final = amt;
	} else if (200 <= amt && amt <= 500) {
		final = 0.9*amt;
	} else {
		final = 0.8*amt;
	}

	printf("%.2f", final);
	return 0;
}