# LMS.py
# Directory: Library Management System
# File: LMS.py

class Book:
    def __init__(self, title, author, pages):
        """
        Initialize the Book object with title, author, and pages.
        """
        self.set_title(title)
        self.set_author(author)
        self.set_pages(pages)
    
    def get_title(self):
        """
        Get the title of the book.
        """
        return self._title
    
    def set_title(self, title):
        """
        Set the title of the book. Raises a ValueError if the title is empty.
        """
        if not title:
            raise ValueError("Title cannot be empty")
        self._title = title
    
    def get_author(self):
        """
        Get the author of the book.
        """
        return self._author
    
    def set_author(self, author):
        """
        Set the author of the book. Raises a ValueError if the author is empty.
        """
        if not author:
            raise ValueError("Author cannot be empty")
        self._author = author
    
    def get_pages(self):
        """
        Get the number of pages in the book.
        """
        return self._pages
    
    def set_pages(self, pages):
        """
        Set the number of pages in the book. Raises a ValueError if pages are not a positive integer.
        """
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Pages must be a positive integer")
        self._pages = pages
    
    def reading_time(self, reading_speed=250):
        """
        Calculate the reading time based on the reading speed (words per minute).
        Assumes 300 words per page.
        """
        words_per_page = 300
        total_words = self._pages * words_per_page
        return total_words / reading_speed

class Ebook(Book):
    def __init__(self, title, author, pages, ebook_format):
        """
        Initialize the Ebook object with title, author, pages, and format.
        """
        super().__init__(title, author, pages)
        self.set_format(ebook_format)
    
    def get_format(self):
        """
        Get the format of the ebook.
        """
        return self._format
    
    def set_format(self, ebook_format):
        """
        Set the format of the ebook. Raises a ValueError if the format is empty.
        """
        if not ebook_format:
            raise ValueError("Format cannot be empty")
        self._format = ebook_format
    
    def __str__(self):
        """
        Override the __str__ method to display all attributes of the Ebook.
        """
        return f"Title: {self.get_title()}, Author: {self.get_author()}, Pages: {self.get_pages()}, Format: {self.get_format()}"

# Demonstrate the use of the classes and methods

try:
    # Create an instance of Book
    book = Book("Sparkling Thoughts", "Hafsah Hashmi", 320)
    
    # Demonstrate the use of getter and setter methods
    print("Original Title:", book.get_title())
    print("Original Author:", book.get_author())
    print("Original Pages:", book.get_pages())
    
    # Update the book details
    book.set_title("Khwabdeedd")
    book.set_author("Hafsah Hashmi")
    book.set_pages(230)
    
    print("\nUpdated Title:", book.get_title())
    print("Updated Author:", book.get_author())
    print("Updated Pages:", book.get_pages())
    
    # Calculate reading time
    print("\nReading Time for the book:", book.reading_time(), "minutes")
    
    # Demonstrate the Ebook class
    ebook = Ebook("Forty Rules of Love", "Elif Shafak", 420, "PDF")
    print("\nEbook Details:")
    print(ebook)

except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)

