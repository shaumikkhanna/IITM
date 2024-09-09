#include <stdio.h>
#include <stdlib.h>


struct Employee {
	char name[50];
	int salary;
	struct Employee *next;
};

void employeeList() {
	struct Employee* root_eptr = (struct Employee*) malloc(sizeof(struct Employee));
	
	struct Employee* eptr = root_eptr;
	struct Employee* new_eptr;
	
	int max_salary = -1;
	int input_flag;

	while (1) {
		scanf("%s %d", eptr->name, &(eptr->salary));
		scanf("%d", &input_flag);

		if (eptr->salary > max_salary) {
			max_salary = eptr->salary;
		}

		if (input_flag) {
			new_eptr = (struct Employee*) malloc(sizeof(struct Employee));
			eptr->next = new_eptr;
			eptr = new_eptr;
		} else {
			eptr->next = NULL;
			eptr = root_eptr;
			while (eptr != NULL) {
				if (eptr->salary == max_salary) {
					printf("%s\n", eptr->name);
				}
				eptr = eptr->next;
			}
			return;
		}
	}
}

int main() {
	employeeList();
}
