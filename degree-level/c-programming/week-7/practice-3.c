#include <stdio.h>


int isIncreasingDecresing(int arr[], int size) {
	int p1 = -1;
	int p2 = -1;

	for (int i = 0; i < size-1; ++i) {
		if (arr[i] >= arr[i+1]) {
			p1 = i;
			break;
		}
	}

	for (int i = size-1; i >= 0; --i) {
		if (arr[i] >= arr[i-1]) {
			p2 = i;
			break;
		}
	}

	if (p1 == p2) {
		return p1;
	} else {
		return -1;
	}
}


int main() {
    int size, res;
    scanf("%d", &size);

    int arr[size];
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    printf("%d",isIncreasingDecresing(arr, size));
    return 0;
}