#include <stdio.h>


int fact(int a) {
    if (a == 0) {
        return 1;
    } else {
        return a*fact(a-1);
    }
}


int main() 
{
    int a;
    long int result;
    scanf("%d", &a);
    
    result = fact(a);
    printf("%ld", result);
    
    return 0;
}