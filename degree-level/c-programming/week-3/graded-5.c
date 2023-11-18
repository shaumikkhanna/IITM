#include <stdio.h>

int main()
{
	int age, gender;
	float weight, height, activity, cals;

	scanf("%d", &age);
	scanf("%d", &gender);
	scanf("%f", &weight);
	scanf("%f", &height);
	scanf("%f", &activity);

	if (gender == 1) {
		cals = (88.362+13.397*weight+4.799*height-5.677*age)*activity;
	} else {
		cals = (447.593+9.247*weight+3.098*height-4.33*age)*activity;
	}

	printf("%.2f", cals);
	return 0;
}