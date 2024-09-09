#include <stdio.h>
//Write function below
int calculateRentalCost(int days, int type) {
    switch (type) {
        case 1:
            return 500*days;
        case 2:
            return 700*days;
        case 3:
            return 1000*days;
    }
}
int main() 
{
    int days,type,res;
    scanf("%d",&days);
    scanf("%d",&type);
    res = calculateRentalCost(days,type);
    printf("%d", res);
    return 0;
}