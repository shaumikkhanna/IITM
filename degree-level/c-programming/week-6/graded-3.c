#include <stdio.h>


void second_largest(int* a, int* b, int* c, int* d, int* e, int* res_ptr) {
    int* ptrs[5] = {a, b, c, d, e};
    int* max_ptr;

    if (*a > *b) {
        max_ptr = a; *res_ptr = *b;
    } else {
        max_ptr = b; *res_ptr = *a;
    }

    for (int i = 2; i < 5; ++i) {
        if (*ptrs[i] > *max_ptr) {
            *res_ptr = *max_ptr;
            max_ptr = ptrs[i];
        } else if (*ptrs[i] > *res_ptr) {
            *res_ptr = *ptrs[i];
        }
    }
}


int main()
{
    int a,b,c,d,e,res;
    scanf("%d%d%d%d%d",&a,&b,&c,&d,&e);
    second_largest(&a,&b,&c,&d,&e,&res);
    printf("%d",res);
}