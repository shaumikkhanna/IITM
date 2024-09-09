#include <stdio.h>
//Write recursive function below
int power(int x, int y) {
    if (y == 0) {
        return 1;
    } else {
        return x*power(x, y-1);
    }
}
int main() 
{
    int x,y;
    scanf("%d",&x);
    scanf("%d",&y);
    printf("%d",power(x,y));
    return 0;
}
