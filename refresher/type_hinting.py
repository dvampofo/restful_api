# Type hinting lets the user know what the data type is accepted as an argument
# or what will be returned

# TH: this method takes in a list and returns a float val
def list_avg(sequence: list) -> float:
    return sum(sequence) / len(sequence)
list_avg(123)

from typing import List # Typle, set, etc

class Book:
    pass

class BookShelf:
    # Takes in a list of books
    def __init__(self, books: List[Book]) -> None:
        self.books = books
    
    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."
    
    