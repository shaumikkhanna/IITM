#include <stdio.h>


struct Student {
    int rollNumber;
    char name[100];
    int marks;
};

void createArray(struct Student* sptr, int n) {
    for (int i = 0; i < n; i++) {
        scanf("%d %s %d", &((sptr+i)->rollNumber), (sptr+i)->name, &((sptr+i)->marks));
    }
}


int main() 
{
    int n;
    scanf("%d", &n);
    struct Student arr[n];
    createArray(arr, n);
    for (int i = 0; i < n; i++) 
    {       
        printf("%d-%s-%d\n",arr[i].rollNumber,arr[i].name,arr[i].marks);
    }
    return 0;
}