#include<stdio.h>


void func(int n) {
    for (int i = n; i > 1; i--) {
        printf("%d ", i);
    }
    printf("1\n");
}


void print_pattern(int n) {
    if (n == 1) {
        printf("1");
        return;
    }
    
    for (int i = 1; i <= n; i++) {
        func(i);
    }

    for (int i = n-1; i > 1; i--) {
        func(i);
    }
    printf("1");
}


int main()
{
    int n;
    scanf("%d",&n);
    print_pattern(n);
    return 0;
}
