#include <stdio.h>
#include <string.h>


struct Score {
	int rollno;
	int marks;
};


void findGreaterThanAverage(struct Score scores[], int n) {
	float avg = 0;
	for (int i = 0; i < n; i++) {
		avg += scores[i].marks;
	}
	avg = avg / n;

	for (int i = 0; i < n; i++) {
		if (scores[i].marks > avg) {
			printf("%d\n", scores[i].rollno);
		}
	}
}



int main()
{
int n;
scanf("%d", &n);
struct Score scores[n];
for (int i = 0; i < n; i++)
{
scanf("%d",&scores[i].rollno);
scanf("%d",&scores[i].marks);
}
findGreaterThanAverage(scores, n);
return 0;
}