#include <stdio.h>
//Write function below
int count_digits(int d, long n) {
    int total = 0;
    int last;

    if (n < 0) {
        n = -n;
    }

    while (n > 0) {
        last = n % 10;
        if (last == d) {
            total++;
        }
        n = n / 10;
    }

    return total;
}
int main(){
    int d;
    long int n;
    scanf("%d %ld",&d,&n);
    printf("%d",count_digits(d,n));
}