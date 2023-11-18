#include <stdio.h>


int main() {
    unsigned int a; 
    scanf("%08X", &a);

    unsigned short* c = (unsigned short*) &a;

    short temp = c[0];
    c[0] = c[1];
    c[1] = temp;

    printf("%08X", a);
    return 0;
}