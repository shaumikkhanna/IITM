#include <stdio.h>

int main() 
{
    float radius;
    float pi = 22.0/7.0;
    scanf("%f", &radius);

	// Write solution code below
    float volume = (4.0/3)*pi*radius*radius*radius;

    printf("%.2f", volume);    
    return 0;
}