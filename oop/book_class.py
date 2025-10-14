class Book:
    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message when the book object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a readable string representation of the Book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an unambiguous string representation for recreating the Book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
