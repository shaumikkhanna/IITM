#include <stdio.h>


int sumNaturalNumbers(int N) {
    if (N == 1) {
        return 1;
    } else {
        return N + sumNaturalNumbers(N - 1);
    }
}


int main() 
{
    int N;
    scanf("%d",&N);
    printf("%d",sumNaturalNumbers(N));
    return 0;
}