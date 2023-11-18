#include <stdio.h>


void findLeaders(int arr[], int n) {
    int flag = 1;
    int leader_candidate, is_leader;

    for (int i = 0; i < n-1; ++i) {
        leader_candidate = arr[i];

        // Check if arr[i] is a leader
        is_leader = 1;
        for (int j = i + 1; j < n; ++j) {
            if (arr[j] > leader_candidate) {
                is_leader = 0;
                break;
            }
        }

        if (is_leader) {
            flag = 0;
            printf("%d\n", leader_candidate);
        }

    }

    if (flag) {
        printf("None");
    }
}



int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
        }       
    findLeaders(arr,n);
    return 0;
}