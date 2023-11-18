#include<stdio.h>


char get_char(char* a, int n) {
    return *(a+n-1);
}


int main()
{
    int n;
    char a[100]; 
    scanf("%s",a);
    scanf("%d",&n);
    printf("%c",get_char(&a[0],n));
    return 0;
}