#include <stdio.h>
// Write solution code below
int count_even(int* a) {
	int out = 0;

	for (int i = 0; i < 5; ++i) {
		if (*(a+i) % 2 == 0) out++;
	}

	return out;
}
int main() 
{
int a[5], i, ans;
for (i=0; i<5; i++) scanf("%d", &a[i]);
ans = count_even(a);
printf("%d", ans);
return 0;
}