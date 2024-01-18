class Library:
    def __init__(self, list):
        self.books_list = list
        self.available_books_list = list[:]  # to get a copy of the list. This copy will not get affected by the changes made in the original list
        self.borrowed_books_list = {}
        
    def display_available(self):
        for i in self.available_books_list:
            print(i)
    
    def display_all(self):
        for books in self.books_list:
            print(books)
    
    def display_borrowed(self, name, book):
        if book not in self.books_list:
            print("Incorrect book")
            return
        if book in self.available_books_list:
            self.borrowed_books_list.update({book:name})
            self.available_books_list.remove(book)
            print(f"{name} borrowed {book}")
        else:
            print("The book is already borrowed by " + self.borrowed_books_list[book])
    
    def display_returned(self, book):
        del self.borrowed_books_list[book]
        self.available_books_list.append(book)
    
    
        
if __name__ == "__main__":
    lib_obj = Library(["book1", "book2", "book3", "book4"])
    
    while True:
        print("Welcome to the library. Enter an option")
        print("1.Display available")
        print("2.Display all")
        print("3.Borrow")
        print("4.Return")
        print("5.Quit")
        
        user_choice = int(input())
        if user_choice == 1:
            lib_obj.display_available()
            
        elif user_choice == 2:
            lib_obj.display_all()
        
        elif user_choice == 3:
            name = input("Enter your name: ")
            book = input("Book name: ")
            lib_obj.display_borrowed(name, book)
        
        elif user_choice == 4:
            book = input("Book name to return: ")
            lib_obj.display_returned()
        
        elif user_choice == 5:
            print("Quitting...")
            break
        
        else:
            print("Invalid option")