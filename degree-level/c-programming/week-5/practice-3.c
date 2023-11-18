#include <stdio.h>


int prime_product(int m) {
    for (int i = 2; i <= m; ++i) {
        if (m % i == 0) {
            m /= i;
            break;
        }
    }

    if (m == 1) {
        return 0;
    }

    for (int i = 2; i < m; ++i) {
        if (m % i == 0) {
            return 0;
        }
    }

    return 1;
}


int main() 
{
    int m;
    scanf("%d",&m);
    if (prime_product(m)==1)
    {
        printf("%d is a prime product",m);
    }
    else
    {
        printf("%d is not a prime product",m);
    }
    return 0;
}