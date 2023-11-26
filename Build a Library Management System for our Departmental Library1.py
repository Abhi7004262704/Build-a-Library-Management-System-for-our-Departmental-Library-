#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Book:
    def __init__(self, title, author, ISBN, quantity):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.quantity = quantity

class User:
    def __init__(self, username, name):
        self.username = username
        self.name = name

class Transaction:
    def __init__(self, user, book, date):
        self.user = user
        self.book = book
        self.date = date
def add_book(title, author, ISBN, quantity):
    # Add a book to the library inventory
    pass

def remove_book(ISBN):
    # Remove a book from the library inventory
    pass

def search_books(keyword):
    # Search for books by title, author, or ISBN
    pass

def check_out_book(username, ISBN):
    # Check out a book to a user
    pass

def check_in_book(ISBN):
    # Check in a book from a user
    pass

def view_transaction_history(username):
    # View transaction history for a user
    pass
while True:
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Books")
    print("4. Check Out Book")
    print("5. Check In Book")
    print("6. View Transaction History")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Take input for book details and call add_book function
        pass
    elif choice == "2":
        # Take input for ISBN and call remove_book function
        pass
    elif choice == "3":
        # Take input for search keyword and call search_books function
        pass
    elif choice == "4":
        # Take input for username and ISBN, then call check_out_book function
        pass
    elif choice == "5":
        # Take input for ISBN and call check_in_book function
        pass
    elif choice == "6":
        # Take input for username and call view_transaction_history function
        pass
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")
# Example using SQLite
import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Create tables for books, users, transactions, etc.

# Modify functions to interact with the database


# In[ ]:




