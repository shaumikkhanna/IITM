#include<stdio.h>

void store_numbers(int *p, int n)
{
   //Write code below
    int temp;
    for (int i = 0; i < n; ++i) {
        scanf("%d", &temp);
        *(p+i) = temp;
    }
}

int main()
{
    int n;
    int a[100]; 
    scanf("%d",&n);
    store_numbers(&a[0],n);
    for(int i=0;i<n;i++)
        {
            printf("%d " ,a[i]);
        }
    return 0;
}