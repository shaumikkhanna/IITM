#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%i", &a);
    scanf("%i", &b);
    scanf("%i", &c);
    
    int R = a*a*a + b*b*b + c*c*c + 3*a*b*c - 2*(a+b+c);
    printf("%i", R);
    return 0;
}