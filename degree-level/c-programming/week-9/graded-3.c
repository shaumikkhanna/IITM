#include <stdio.h>


int countFrom2DArray(int a[10][10], int r, int c, int search) {
	int count = 0;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			if (a[i][j] == search) {
				count++;
			}
		}
	}
	return count;
}


int main() {
	int a[10][10], r, c, search;
	scanf("%d", &r);
	scanf("%d", &c);

	for (int i = 0; i < r; i++)
	{
	for (int j = 0; j < c; j++) 
	{
		scanf("%d", &a[i][j]);
	}
	}

	scanf("%d", &search);
	int count = countFrom2DArray(a, r, c, search);
	printf("%d", count);

	return 0;
}
