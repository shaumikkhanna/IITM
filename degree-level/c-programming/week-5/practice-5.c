#include <stdio.h>
#include <math.h>


int nth_digit(int num, int n) {
	if (n == 0 || n > ceil(log10(num))) {
		return -1;
	}

	int last;

	for (int i = 0; i < n; ++i) {
		last = num % 10;
		num /= 10;
	}

	return last;
}



int main(){
    int num, n;
    scanf("%d %d", &num, &n);
    printf("%d", nth_digit(num, n));
}