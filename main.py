class Library:
    def __init__(shelf, listOfBooks):
        shelf.books = listOfBooks

    def displayAvailableBooks(shelf):
        print("Books present in this library are: ")
        for book in shelf.books: 
            print("*" + book)
    
    def borrowBook(shelf, bookName):
        if bookName in shelf.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            shelf.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(shelf, bookName):
        shelf.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student: 
    def requestBook(shelf):
        shelf.book = input("Enter the name of the book you want to borrow: ")
        return shelf.book

    def returnBook(shelf):
        shelf.book = input("Enter the name of the book you want to return: ")
        return shelf.book
         

if __name__ == "__main__":
    centralLibrary = Library(["Wings of Fire", "Ikigai", "The Secret", "Python Notes"])
    student = Student()
    centralLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")

        
