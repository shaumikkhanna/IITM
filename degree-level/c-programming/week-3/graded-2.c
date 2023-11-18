#include <stdio.h>
#include <math.h>

int main() 
{
    //Initialization of variables
    float principal, annualRate, monthlyRate, monthlyPayment;
    int numMonths;
    
	//Reading Inputs
    scanf("%f", &principal);
    scanf("%f", &annualRate);
    scanf("%d", &numMonths);
    // Write code below to calculate the monthly payment and store the result in monthlyPayment variable

    monthlyRate = annualRate / 12 / 100;
    monthlyPayment = principal*monthlyRate*pow(1+monthlyRate,numMonths) / (pow(1+monthlyRate,numMonths) - 1);

   //Printing the output
    printf("%.2f", monthlyPayment);
    return 0;
}
