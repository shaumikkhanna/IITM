#include <stdio.h>


struct Data {
    int num1;
    int num2;
    int op;
};


void calculator(struct Data data) {
    switch (data.op) {
        case 1:
            printf("%d", data.num1 + data.num2); break;
        case 2:
            printf("%d", data.num1 - data.num2); break;
        case 3:
            printf("%d", data.num1 * data.num2); break;
        case 4:
            if (data.num2 == 0) {
                printf("Zero Division Error");
            } else {
                printf("%.2f", (float)data.num1 / data.num2);
            }
    }
}


int main() {
    struct Data data;

    scanf("%d", &data.num1);
    scanf("%d", &data.num2);
    scanf(" %d", &data.op);

    calculator(data);

    return 0;
}