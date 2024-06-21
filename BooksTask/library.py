import json
from book import Book

class Library:
    def __init__(self, filename="library.json"):
        """
        Initialize a Library object.

        Args:
        - filename (str, optional): File name to save/load library data (default is 'library.json').
        """
        self.filename = filename
        self.books = []
        self.load_library()

    def add_book(self, book):
        """
        Add a book to the library and save library data to file.

        Args:
        - book (Book): Book object to add to the library.
        """
        self.books.append(book)
        self.save_library()

    def list_books(self, author=None, genre=None):
        """
        Retrieve a list of books from the library based on optional filters.

        Args:
        - author (str, optional): Filter books by author.
        - genre (str, optional): Filter books by genre.

        Returns:
        - list: List of Book objects filtered by author and/or genre.
        """
        filtered_books = self.books
        if author:
            filtered_books = [book for book in filtered_books if book.author == author]
        if genre:
            filtered_books = [book for book in filtered_books if book.genre == genre]
        return filtered_books

    def edit_book(self, title, new_details):
        """
        Edit details of a specific book in the library and save library data to file.

        Args:
        - title (str): Title of the book to edit.
        - new_details (dict): Dictionary containing new details for the book (title, author, publication_year, genre).
        """
        for book in self.books:
            if book.title == title:
                book.update(**new_details)
                self.save_library()
                return True
        return False

    def delete_book(self, title):
        """
        Delete a specific book from the library and save library data to file.

        Args:
        - title (str): Title of the book to delete.
        """
        self.books = [book for book in self.books if book.title != title]
        self.save_library()

    def save_library(self):
        """
        Save the current state of the library (books) to a JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file)

    def load_library(self):
        """
        Load library data from a JSON file into the library (books).
        If the file does not exist, initialize an empty library.
        """
        try:
            with open(self.filename, 'r') as file:
                book_dicts = json.load(file)
                self.books = [Book(**book_dict) for book_dict in book_dicts]
        except FileNotFoundError:
            self.books = []
