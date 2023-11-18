#include <stdio.h>
#include <string.h>
#define MAX_LEN 100


void reverse(char* string) {
    int n = strlen(string);
    char temp;

    for (int i = 0; i < n/2; ++i) {
        temp = string[i];
        string[i] = string[n-1-i];
        string[n-1-i] = temp;
    }

    printf("%s", string);
}

int main() 
{
    char input_str[MAX_LEN]="";

    // Input
    fgets(input_str, sizeof(input_str), stdin);
    // Remove the newline character from the input string
    if (input_str[strlen(input_str) - 1] == '\n') {
        input_str[strlen(input_str) - 1] = '\0';
    }    
    // Output
    reverse(input_str);
    return 0;
}