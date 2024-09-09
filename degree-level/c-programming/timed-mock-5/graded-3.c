#include <stdio.h>
#include <string.h>


struct Person {
	char name[100];
	int age;
	char city[100];
};


void findYoungestPersons(struct Person people[], int n) {
	int min_age = people[0].age;
	for (int i = 1; i < n; i++) {
		if (people[i].age < min_age) {
			min_age = people[i].age;
		}
	}
	for (int i = 0; i < n; ++i) {
		if (people[i].age == min_age) {
			printf("%s: %s\n", people[i].name, people[i].city);
		}
	}
}



int main()
{
int n;
scanf("%d", &n);
struct Person persons[n];
for (int i = 0; i < n; i++)
{
scanf("%s",persons[i].name);
scanf("%d",&persons[i].age);
scanf("%s",persons[i].city);
}
findYoungestPersons(persons, n);
return 0;
}