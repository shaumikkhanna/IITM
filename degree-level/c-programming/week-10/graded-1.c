#include <stdio.h>
#include <stdlib.h>


void writeToFile() {
    char user[50];
    fgets(user, 50, stdin);

    FILE* fp = fopen("notes.txt", "w");

    fputs(user, fp);

    fclose(fp);
}



int main() 
{
    char s[20];
    writeToFile();
    FILE *fp = fopen("notes.txt", "r");
    fgets(s, 20, fp);
    printf("%s", s);
    fclose(fp);
    return 0;
}