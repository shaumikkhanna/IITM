#include<stdio.h>
//Write function below
void print_xo_pattern(int n) {
    if (n < 1) {
        printf("INVALID");
        return;
    }

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= i/2; ++j) {
            printf("xo");
        }
        if (i % 2 == 1) {
            printf("x");
        }
        printf("\n");
    }
}
int main()
{
    int n;
    scanf("%d", &n);
    print_xo_pattern(n);
    return 0;
}
