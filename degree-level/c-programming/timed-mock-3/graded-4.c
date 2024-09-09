#include<stdio.h>
//Write solution code below
#include <math.h>

void DecimalToBinary(int D, long int* B) {
    if (D == 0) {
        *B = 0; return;
    }

    int T = floor(log2(D));

    D -= pow(2, T);
    long int out = 1;
    T--;

    while (T >= 0) {
        int place = pow(2, T);
        if (D >= place) {
            D -= place;
            out = 10*out + 1;
        } else {
            out = 10*out;
        }
        T--;
    }

    *B = out;
}
int main()
{
    int D;
    long int B; 
    scanf("%d",&D);    
    DecimalToBinary(D, &B);
    printf("%ld", B);
    return 0;
}
