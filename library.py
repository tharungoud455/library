class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

    #Display method to display the book information
    def displayBookInfo(self):
        print(f"BookTitle:{self.title}\nAuthor:{self.author}\nISBN:{self.isbn}")
class Library:
    def __init__(self):
        self.booksList=[] #intialize list with empty values
    def addBook(self,book):
        if isinstance(book,Book):
            self.booksList.append(book)
        else:
            print("Invalid book type!")
    def displayAllBooks(self):
        if len(self.booksList):
            for book in (self.booksList):
                book.displayBookInfo() #calling disply method to show book information
                print()
        else:
            print("No Books available!")
    def searchBookByTitle(self,title):
        for book in self.booksList:
            if book.title.lower() == title.lower():
                return book
        return None

class EBook(Book):    #inherits from parent Book class
    def __init__(self,title,author,isbn,fileFormat):
        super().__init__(title,author,isbn)  #Calling parent constructor
        self.fileFormat = fileFormat   #Additional attribute of e-book
    def displayBookInfo(self):
        super().displayBookInfo()
        print(f"File Format:{self.fileFormat}")

#Test code

try:
    book1=Book("The God of Small Things","Arundhati Roy","978-0-06-090605-0")
    book2=Book("India After Gandhi","Ramachandra Guha","978-0-670-04360")
    ebook1=EBook("The Argumentative Indian","Amartya Sen","978-0-14-306359-5","PDF")
    library=Library()
    library.addBook(book1)
    library.addBook(book2)
    library.addBook(ebook1)
except Exception as e:
    print("ERROR FOUND:",e)
finally:
    print("\nDisplay all books:\n")

#searching for a book

library.displayAllBooks()
inputTitle=input("Enter the Book Title To search:")
result=library.searchBookByTitle(inputTitle)
if result:
    print("Seached Book Infprmation")
    result.displayBookInfo()
else:
    print("No Such Book Found!")