#include <stdio.h>
//Write Solution code below
int fact(int n) {
    if (n == 0) {
        return 1;
    } else {
        return n*fact(n-1);
    }
}

void factorial(int* a, int* b) {
    *b = fact(*a);
}
int main() 
{
    int a, b;
    scanf("%d", &a);    
    factorial(&a, &b);    
    printf("%d", b);    
    return 0;
}
