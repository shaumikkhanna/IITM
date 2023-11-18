#include <stdio.h>


int nth_fibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;

    return nth_fibonacci(n-1) + nth_fibonacci(n-2);
}



int main() 
{
    int n;
    scanf("%d",&n);
    printf("%d",nth_fibonacci(n));
    return 0;
}