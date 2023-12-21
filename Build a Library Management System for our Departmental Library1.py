import tkinter as tk
from tkinter import messagebox

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Abhi@123", 
    database="L_M_S"
)
class Book:
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

class Patron:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []
        self.transactions = []

    def add_book(self, book):
        self.books.append(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron, book):
        if book.available_copies > 0:
            book.available_copies -= 1
            transaction = {'patron': patron.name, 'book': book.title, 'action': 'borrow'}
            self.transactions.append(transaction)
            messagebox.showinfo("Borrow Book", f"{patron.name} has borrowed {book.title}.")
        else:
            messagebox.showinfo("Borrow Book", f"Sorry, {book.title} is not available for borrowing.")

    def return_book(self, patron, book):
        book.available_copies += 1
        transaction = {'patron': patron.name, 'book': book.title, 'action': 'return'}
        self.transactions.append(transaction)
        messagebox.showinfo("Return Book", f"{patron.name} has returned {book.title}.")

class LibraryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")

        self.library = Library()

        # Create widgets
        self.book_label = tk.Label(root, text="Book Title:")
        self.book_entry = tk.Entry(root)
        self.author_label = tk.Label(root, text="Author:")
        self.author_entry = tk.Entry(root)
        self.copies_label = tk.Label(root, text="Available Copies:")
        self.copies_entry = tk.Entry(root)
        self.add_book_button = tk.Button(root, text="Add Book", command=self.add_book)

        self.patron_label = tk.Label(root, text="Patron Name:")
        self.patron_entry = tk.Entry(root)
        self.borrow_book_button = tk.Button(root, text="Borrow Book", command=self.borrow_book)
        self.return_book_button = tk.Button(root, text="Return Book", command=self.return_book)

        # Layout
        self.book_label.grid(row=0, column=0, padx=10, pady=10)
        self.book_entry.grid(row=0, column=1, padx=10, pady=10)
        self.author_label.grid(row=1, column=0, padx=10, pady=10)
        self.author_entry.grid(row=1, column=1, padx=10, pady=10)
        self.copies_label.grid(row=2, column=0, padx=10, pady=10)
        self.copies_entry.grid(row=2, column=1, padx=10, pady=10)
        self.add_book_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.patron_label.grid(row=4, column=0, padx=10, pady=10)
        self.patron_entry.grid(row=4, column=1, padx=10, pady=10)
        self.borrow_book_button.grid(row=5, column=0, pady=10)
        self.return_book_button.grid(row=5, column=1, pady=10)

    def add_book(self):
        title = self.book_entry.get()
        author = self.author_entry.get()
        copies = int(self.copies_entry.get())
        book = Book(title, author, copies)
        self.library.add_book(book)
        messagebox.showinfo("Add Book", f"Book '{title}' added to the library.")

    def borrow_book(self):
        patron_name = self.patron_entry.get()
        book_title = self.book_entry.get()
        patron = Patron(patron_name)

        # Check if the book exists
        book = next((b for b in self.library.books if b.title == book_title), None)
        if book:
            self.library.borrow_book(patron, book)
        else:
            messagebox.showinfo("Borrow Book", f"Book '{book_title}' not found in the library.")

    def return_book(self):
        patron_name = self.patron_entry.get()
        book_title = self.book_entry.get()
        patron = Patron(patron_name)

        # Check if the book exists
        book = next((b for b in self.library.books if b.title == book_title), None)
        if book:
            self.library.return_book(patron, book)
        else:
            messagebox.showinfo("Return Book", f"Book '{book_title}' not found in the library.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementApp(root)
    root.mainloop()
