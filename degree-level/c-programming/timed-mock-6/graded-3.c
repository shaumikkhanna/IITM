#include <stdio.h>
#include <stdlib.h>

typedef struct{
    int** vals;
    int dim0;
    int dim1;
} Array2D;


Array2D inverted_identity_matrix(int n) {
     int** mat = (int**) malloc(n * sizeof(int*));
     for (int i = 0; i < n; i++) {
        mat[i] = (int*) malloc(n * sizeof(int));
     }

     for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            mat[i][j] = (i == j) ? 0 : 1;
        }
     }

     Array2D out = {mat, n, n};
     return out;
}


void print_array2d(Array2D* a) {
    for (int i = 0; i < a->dim0; i++) {
        for (int j = 0; j < a->dim1 - 1; j++) {
            printf("%d ", a->vals[i][j]);
        }
        printf("%d\n", a->vals[i][a->dim1-1]);
    }
}


void free_array2d(Array2D* a) {
    for (int i=0;i<a->dim0;i++){
        free(a->vals[i]);
    }
    free(a->vals);
}

int main(){
    int n;
    scanf("%d",&n);
    Array2D a = inverted_identity_matrix(n);
    print_array2d(&a);
    free_array2d(&a);
    return 0;    
}
