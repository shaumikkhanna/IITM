#include <stdio.h>
#include <stdlib.h>

typedef struct{
    int* vals;
    int len;
} Array;



Array create_range(int start, int end, int step) {
    Array arr;
    arr.len = (end - start) / step + 1;
    arr.vals = (int*) malloc(arr.len * sizeof(int));

    for (int i = 0; i < arr.len; i++) {
        arr.vals[i] = start + i*step;
    }
    return arr;
}


void print_array(Array a){
    for (int i =0;i<a.len;i++){
        printf("%d ", a.vals[i]);
    }
}

int main() {
    int start, end, step;
    scanf("%d %d %d", &start,&end,&step);

    Array r = create_range(start,end,step);
    print_array(r);

    // Free the dynamically allocated memory
    free(r.vals);

    return 0;
}