#include<stdio.h>


void min_max_swap(int* a, int* b, int* c, int* d, int* e) {
    int* ptrs[5] = {a, b, c, d, e};
    int* max_ptr = ptrs[0];
    int* min_ptr = ptrs[0];

    for (int i = 1; i < 5; ++i) {
        if (*ptrs[i] > *max_ptr) {
            max_ptr = ptrs[i];
        }
        if (*ptrs[i] < *min_ptr) {
            min_ptr = ptrs[i];
        }
    }

    int temp = *max_ptr;
    *max_ptr = *min_ptr;
    *min_ptr = temp;
}


int main()
{
    int a,b,c,d,e;
    scanf("%d%d%d%d%d",&a,&b,&c,&d,&e);
    min_max_swap(&a,&b,&c,&d,&e);
    printf("%d %d %d %d %d",a,b,c,d,e);
}