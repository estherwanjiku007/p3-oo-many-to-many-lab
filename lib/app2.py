#many to many rel
#always involves an association table
class Book:
    book_count=0
    def __init__(self,title) -> None:
        self.name=title
        self.authors=[]
        Book.book_count+=1

    def add_author(self,author):
        self.authors.append(author)
        author.books.append(self)

class Author:
    author_count=0
    def __init__(self,name) -> None:
        self.name=name
        self.books=[]
        Author.author_count+=1

    def write_book(self,book):
        self.books.append(book)
        book.authors.append(self)

class Authorship:#Creates the relationship of the author and the book class
    def __init__(self,book,author) -> None:
        self.book=book
        self.author=author

book1=Book("Money")
book2=Book("Salvation")
author1=Author("Beatrice")
author2=Author("Esther")
#authorship1=Authorship()
for author in [author1,author2]:
    print(f"{author.name} has the following books:")
    for book in author.books:
        print(f"{book.title}")

for book in [book1,book2]:
    print(f"{book.title } was written by the following authors:" )
    for author in book.authors:
        print(f"{author.name}")
    