#include <stdio.h>
#include <stdlib.h>



int** twoDimArray(int row, int col) {
    int** out = (int**) malloc(row * sizeof(int*));
    for (int i = 0; i < row; i++) {
        out[i] = (int*) malloc(col * sizeof(int));
    }

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            out[i][j] = 0;
        }
    }

    return out;
}


int main()
{   
    int i,j;
    int row,col;
    scanf("%d", &row);
    scanf("%d", &col);
    int **p = twoDimArray(row, col);
    for(i=0;i<row;i++)
    {   
        for(j=0;j<col;j++)
        {
            printf("%d ",*(*(p + i) + j));
        }
        printf("\n");
    }
}