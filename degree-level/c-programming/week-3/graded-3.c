#include <stdio.h>

int main()
{
	float weight, rate, cost;

	scanf("%f", &weight);
	scanf("%f", &rate);

	cost = weight*rate;

	printf("%.2f", cost);
	
	return 0;

}