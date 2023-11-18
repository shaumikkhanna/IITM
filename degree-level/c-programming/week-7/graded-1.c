#include <stdio.h>


int find_frequency(int a[], int n) {
    int out = 0;

    for (int i = 0; i < 5; i++) {
        if (a[i] == n) {
            out++;
        }
    }

    return out;
}


int main() {
    int a[5], n, i, ans;
    scanf("%d", &n);

    for (i=0; i<5; i++) scanf("%d", &a[i]);
    ans = find_frequency(a, n);
    printf("%d", ans);

    return 0;
}