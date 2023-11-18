#include <stdio.h>


int main()
{
    int n, i, a[10], sum=0;
    
    //Write code below
    scanf("%d",&n);
    int input;

    for (int i = 0; i < n; ++i) {
        scanf("%d",&input);
        a[i] = input;
        sum += input;
    }

    for (i=0; i<n; i++) printf("%d ",a[i]);
    printf("\n%d", sum);

    return 0;
}