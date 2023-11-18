#include <stdio.h>
#include <math.h>


int isArmstrong(int n) {
    if (n==1) {
        return 1;
    }

    int power = ceil(log10(n));
    int num = n;
    int out = 0;

    for (int i = 0; i < power; ++i) {
        out += pow(n % 10, power);
        n /= 10;
    }

    return (num==out);
}


void countArmstrong(int* a, int* b, int* count) {
    int out = 0;

    for (int i = *a; i <= *b; ++i) {
        if (isArmstrong(i)) {
            out++;
        }
    }

    *count = out;
}


int main() 
{
    int a,b,count;
    scanf("%d %d",&a,&b);
    countArmstrong(&a,&b,&count);
    printf("%d",count);
    return 0;
}
