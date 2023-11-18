#include <stdio.h>


void calculate_sum(int a, int b, int* p) {
    int total = a + b;
    *p = a+b;
}


int main() 
{
    int a, b, c = 0;
    
    scanf("%d", &a);
    scanf("%d", &b);
    
    calculate_sum(a, b, &c);
    
    printf("%d", c);
    
    return 0;
}