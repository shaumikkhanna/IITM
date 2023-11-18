#include <stdio.h>
#include <math.h>

int main() 
{
    float principal, rate, time;
	scanf("%f%f%f", &principal,&rate,&time);

	// Write solution code below
	float simpleInterest = principal*rate*time / 100;

	printf("%.2f", simpleInterest);
    return 0;
}