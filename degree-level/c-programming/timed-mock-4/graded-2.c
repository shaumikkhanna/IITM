#include <stdio.h>
//Write solution code below
int isIncreasing(int arr[], int size) {
    for (int i = 0; i < size-1; ++i) {
        if (arr[i] >= arr[i+1]) {
            return 0;
        }
    }
    return 1;
}
int main() 
{
    int size, res;
    scanf("%d", &size);

    int arr[size];
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    res = isIncreasing(arr, size);
    if(res == 1)
    {
        printf("True");
    }
    else
    {
        printf("False");
    }
    

    return 0;
}

