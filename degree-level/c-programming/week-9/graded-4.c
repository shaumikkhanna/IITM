#include <stdio.h>


int diagonalSum(int n, int arr[n][n]) {
	int out = 0;
	for (int i = 0; i < n; i++) {
		out += arr[i][i];
	}
	return out;
}


int main() 
{
int N;
scanf("%d", &N);
int matrix[N][N];
for (int i = 0; i < N; i++)
{
for (int j = 0; j < N; j++)
{
scanf("%d", &matrix[i][j]);
}
}
printf("%d\n",diagonalSum(N,matrix));
return 0;
}
