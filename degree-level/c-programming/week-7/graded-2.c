#include <stdio.h>



void reverseArray(int arr[], int size) {
    int temp;

    for (int i = 0; i < size/2; ++i) {
        temp = arr[i];
        arr[i] = arr[size-1-i];
        arr[size-1-i] = temp;
    }
}


int main() 
{
    int n;
    scanf("%d", &n);

    int arr[n];
    for (int i = 0; i < n; i++) 
    {
        scanf("%d", &arr[i]);
    }

    reverseArray(arr, n);

    for (int i = 0; i < n; i++) 
    {
        printf("%d ", arr[i]);
    }

    return 0;
}