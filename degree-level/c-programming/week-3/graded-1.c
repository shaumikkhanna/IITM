#include <stdio.h>
#include <math.h>

int main() 
{
    // Initialization of Variables
    float diameter, costPerSqInch, costperTopping, totalCost;
    int numToppings;
	
    // Reading Input
    scanf("%f", &diameter);
    scanf("%f", &costPerSqInch);
    scanf("%d", &numToppings);
    scanf("%f", &costperTopping);  
    // Write code below to calculate the total cost and store the result in totalCost variable
    
    totalCost = 3.14*(diameter/2)*(diameter/2)*costPerSqInch + numToppings*costperTopping;
    
    // Print the total cost
    printf("%.2f", totalCost);
    return 0;
}