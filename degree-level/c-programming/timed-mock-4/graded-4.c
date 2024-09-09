#include <stdio.h>
#include <string.h>
void countVowelsConsonants(const char* str, int* vowels, int* consonants) {
    char my_char;
    int count_vowels = 0;
    int count_consonants = 0;

    for (int i = 0; i < strlen(str); i++) {
        my_char = str[i];
        if (my_char == 97 || my_char == 101 || my_char == 105 || my_char == 111 || my_char == 117) {
            count_vowels++;
        } else {
            count_consonants++;
        }
    }

    *vowels = count_vowels;
    *consonants = count_consonants;
}
int main() 
{
    char inputString[99];
    scanf("%s", inputString);

    int numVowels, numConsonants;
    countVowelsConsonants(inputString, &numVowels, &numConsonants);

    printf("Vowels: %d\n", numVowels);
    printf("Consonants: %d\n", numConsonants);

    return 0;
}
