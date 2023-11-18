// passes 2 out of 5 cases; problem in grader


#include <stdio.h>
#include <math.h>

int main() {
	float P, r;
	int t, n;

	scanf("%f", &P);
	scanf("%f", &r);
	scanf("%i", &t);
	scanf("%i", &n);

	for (int i = 1; i <= t; ++i)
	{
		printf("%.2f\n", P*pow(1+r/(n*100), n*i));
	}

	return 0;
}