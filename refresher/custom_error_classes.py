class TooManyPageError(ValueError):
    # inheriting from the ValueError class
    pass

class Book:
    def __init__(self, name: str, page_count: int) -> None:
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr__(self) -> str:
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )
    
    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPageError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}")
        
book1 = Book("Dune", 500)
book1.read(3000)

