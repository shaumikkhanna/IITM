#include <stdio.h>


void displayElements(int n, int m, int matrix[n][m], char c) {
	if (c == 'R') {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				printf("%d ", matrix[i][j]);
			}
		}
	} else {
		for (int j = 0; j < m; j++) {
			for (int i = 0; i < n; i++) {
				printf("%d ", matrix[i][j]);
			}
		}
	}
}



int main()
{
int N,M;
char type;
scanf("%d %d %c",&N,&M,&type);
//scanf("%c",&type);
int matrix[N][M];
for (int i = 0; i < N; i++)
{
for (int j = 0; j < M; j++)
{
scanf("%d", &matrix[i][j]);
}
}
displayElements(N,M,matrix,type);
return 0;
}