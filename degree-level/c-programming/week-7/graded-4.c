#include <stdio.h>

int max_index(int arr[], int size) {
    int max = arr[0];
    int max_index = 0;

    for (int i = 1; i < size; i++) {
        if (arr[i] >= max) {
            max = arr[i];
            max_index = i;
        }
    }

    return max_index;
}

int main() 
{
    int N;
    scanf("%d", &N);

    int arr[N];
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }
    int maxIndex = max_index(arr,N);
    printf("%d\n", maxIndex);
    return 0;
}