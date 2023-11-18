#include <stdio.h>

int main() 
{
    int n;
    scanf("%d", &n);
	
    // Write solution code below
    int sum = n*(n+1) / 2;

    printf("%d",sum);    
    return 0;
}