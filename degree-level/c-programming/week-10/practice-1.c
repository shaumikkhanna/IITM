// ONE TEST CASE NOT PASSED

#include <stdio.h>


void createFile(int arr[], int n) {
	FILE* fp;
	if ((fp = fopen("output.txt", "w")) == NULL) {
		printf("Oops");
	}

	for (int i = 0; i < n; i++) {
		fprintf(fp, "%d\n", arr[i]);
	}

	fclose(fp);
}
