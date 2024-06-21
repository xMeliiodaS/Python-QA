from flask import Flask, request, render_template, redirect, url_for
from library import Library
from book import Book

app = Flask(__name__)
library = Library()


@app.route('/')
def index():
    """
    Render the index.html template for the home page.
    """
    return render_template('index.html')


@app.route('/books', methods=['GET', 'POST'])
def books():
    """
    Handle GET (list books) and POST (add book) requests for the books page.
    """
    if request.method == 'POST':
        data = request.form
        book = Book(data['title'], data['author'], int(data['year']), data['genre'])
        library.add_book(book)
        return redirect(url_for('books'))

    books = library.list_books()
    return render_template('books.html', books=books)


@app.route('/edit/<title>', methods=['GET', 'POST'])
def edit_book(title):
    """
    Handle GET (render edit form) and POST (update book details) requests for editing a book.
    """
    book = next((book for book in library.books if book.title == title), None)
    if not book:
        return redirect(url_for('books'))

    if request.method == 'POST':
        data = request.form
        new_details = {
            "title": data.get('new_title'),
            "author": data.get('author'),
            "publication_year": int(data.get('year')),
            "genre": data.get('genre')
        }
        library.edit_book(title, new_details)
        return redirect(url_for('books'))

    return render_template('edit_book.html', book=book)


@app.route('/delete/<title>')
def delete_book(title):
    """
    Handle deleting a book from the library.
    """
    library.delete_book(title)
    return redirect(url_for('books'))


if __name__ == '__main__':
    app.run(debug=True)
