#many to many rel
#here,we use the intermediary
#register the skillset of meachanics in my garage
#Mechanic-name,sttaff no,skill
#Skill-id,skillid,name
#mechanic_skill
#id|meachanicid|skillid
#BOOKS AND AUTHORS-
class Book:
    book_count=0

    def __init__(self,title):
        self.title=title
        self.author=[]
        Book.book_count+=1

    def add_author(self,author):
        self.author.append(author)
        author.books.append(self)

class Author:
    author_count=0
    def __init__(self,name):
        self.name=name
        self.books=[]
        Author.author_count+=1

    def write_book(self,book):
        self.books.append(book)
        book.author.append(self)

    