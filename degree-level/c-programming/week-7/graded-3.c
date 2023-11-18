#include <stdio.h>


int findIntersection(int arr1[], int arr2[], int n1, int n2) {
    int out = 0;

    for (int i = 0; i < n1; ++i) {
        for (int j = 0; j < n2; ++j) {
            if (arr1[i] == arr2[j]) out++;
        }
    }

    return out;
}


int main() {
    int n1, n2;
    scanf("%d", &n1);

    int arr1[n1];
    for (int i = 0; i < n1; i++) {
        scanf("%d", &arr1[i]);
    }

    scanf("%d", &n2);

    int arr2[n2];
    for (int i = 0; i < n2; i++) {
        scanf("%d", &arr2[i]);
    }

    printf("%d",findIntersection(arr1, arr2, n1, n2));

    return 0;
}