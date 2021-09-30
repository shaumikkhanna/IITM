select book_catalogue.title
from book_authors, book_catalogue
where (book_authors.isbn_no, author_fname, author_lname) = (book_catalogue.isbn_no, 'Joh Paul', 'Mueller')
;