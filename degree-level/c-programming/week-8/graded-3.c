#include <stdio.h>
#include <string.h>



struct Book {
    char title[100];
    char author[100];
    int publication_year;
};


void findBooksPublishedInYear(struct Book arr[], int size, int year) {
    struct Book book;
    int book_found = 0;

    for (int i = 0; i < size; ++i) {
        book = arr[i];
        if (book.publication_year == year) {
            printf("%s: %s\n", book.title, book.author);
            book_found = 1;
        }
    }

    if (!book_found) {
        printf("NONE");
    }
}


int main() 
{
    int n;
    scanf("%d", &n);
    struct Book books[n];
    for (int i = 0; i < n; i++) 
    {       
        scanf("%s",books[i].title);
        scanf("%s",books[i].author);
        scanf("%d",&books[i].publication_year);
    }
    int searchYear;
    scanf("%d", &searchYear);
    findBooksPublishedInYear(books, n, searchYear);

    return 0;
}