//Prefix code
#include<stdio.h>
//main function is hidden, write only required function below

int find_max(int n, int* p) {
    int out = *p;
    for (int i = 1; i < n; i++) {
        if (*(p+i) > out) {
            out = *(p+i);
        }
    }
    return out;
}