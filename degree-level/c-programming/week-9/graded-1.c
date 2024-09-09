#include<stdio.h>
#include<stdlib.h>

struct Student {
    char name[50];
    struct Student *next;
};

struct Student* studentList() {
    struct Student* head = (struct Student*) malloc(sizeof(struct Student));
    struct Student* sptr = head;
    int input_flag;

    while (1) {
        scanf("%s", sptr->name);
        scanf("%d", &input_flag);

        if (input_flag) {
            sptr->next = (struct Student*) malloc(sizeof(struct Student));
            sptr = sptr->next;
        } else {
            sptr->next = NULL;
            return head;
        }
    }
}

int main() {
    struct Student *head;
    head = studentList();
    while (head != NULL) {
        printf("%s\n",head->name);
        head = head->next;
    }
}