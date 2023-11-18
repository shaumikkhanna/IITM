#include <stdio.h>

int main() {
	float weight, cost;
	int zone;

	scanf("%f", &weight);
	scanf("%i", &zone);

	if (weight < 1)
	{
		printf("Invalid Input"); return 0;
	}

	switch (zone) 
	{
	case 1:
		cost = 5*weight; break;
	case 2:
		cost = 7*weight; break;
	case 3:
		cost = 10*weight; break;
	case 4:
		cost = 12*weight; break;
	case 5:
		cost = 16*weight; break;
	case 6:
		cost = 17*weight; break;
	case 7:
		cost = 19*weight; break;
	default:
		printf("Invalid Input"); return 0;
	}

	printf("%.2f", cost);
	return 0;
}