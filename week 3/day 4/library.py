class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display_info(self):
        print('title:', self.title)
        print('author:', self.author)
        print('available:', self.available)

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        
library = Library()

def add_book(library):
    title = input('Title:').strip()
    author = input('Author:').strip()


    new_book = Book(title, author)
    library.add_book(new_book)
    
def view_books(library):
    for book_number, book_details in enumerate(library.books, start=1):
        print(book_number, '] ------------')
        book_details.display_info()

def borrow_book(library):
    book_search = input('book:').strip()

    for book in library.books:
        if book_search.lower() == book.title.lower():
            if book.available:
                book.available = False
                print('Book borrowed')
                return
            else:
                print('Book already borrowed')
                return

    print('Book not found')   


def return_book(library):
    book_return = input('book:').strip()

    for book in library.books:
        if book_return.lower() == book.title.lower():
            if not book.available:
                book.available = True
                print('Book returned!')
                return
            else:
                print('book already available!')
                return

    print('book not found on system')


while True:
    print('---- Library Manager ----')
    print('1. Add book')
    print('2. View book')
    print('3. Borrow book')
    print('4. Retrun book')
    print('5. Exit')
    choice = input('choice:')

    if choice == '1':
        add_book(library)
    elif choice == '2':
        view_books(library)
    elif choice == '3':
        borrow_book(library)
    elif choice == '4':
        return_book(library)
    elif choice == '5':
        print('Have a nice rest of yuor day!')
        break
    else:
        print('Please enter a valid input!')
