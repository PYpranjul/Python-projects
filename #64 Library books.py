
class Library:
    def __init__(self):
        books=[]
        while True:
            add=input("Do you want to add a book to the library? ").strip().lower()
            if  add=="yes":
                book=input("Enter the name of the book you want to add: ") 
                books.append(book)
            else:
                print("The Length of library is:",len(books))
                break
        print(books)
l=Library()
