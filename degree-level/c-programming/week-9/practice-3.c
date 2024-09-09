#include <stdio.h>


void printTranspose(int a[10][10], int r, int c) {
	for (int j = 0; j < c; j++) {
		for (int i = 0; i < r; i++) {
			printf("%d ", a[i][j]);
		}
		printf("\n");
	}
}



int main() 
{
int a[10][10], r, c;
scanf("%d", &r);
scanf("%d", &c);
for (int i = 0; i < r; ++i)
for (int j = 0; j < c; ++j) {
scanf("%d", &a[i][j]);
}
printTranspose(a, r, c);
return 0;
}