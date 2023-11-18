#include <stdio.h>


int main() {
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);    

    int* p = &a;
    *p = b;

    printf("%d", a);
    printf("\n");
    printf("%d", *p);
    
    return 0;
}