class Book:
    def __init__(self, title, author, ratings):
        self.title = title
        self.author = author
        self.ratings = ratings

    def average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0

    def __str__(self):
        return f"Книга: '{self.title}' автора {self.author}, середній рейтинг: {self.average_rating():.2f}"

    def ratings_greater_than(self, number):
        return [rating for rating in self.ratings if rating > number]

book1 = Book("Мистецтво програмування", "Дональд Кнут", [5, 4, 5, 4, 5])
print(book1)
print("Рейтинги > 4:", book1.ratings_greater_than(4))

class Ebook(Book):
    def __init__(self, title, author, ratings, file_size):
        super().__init__(title, author, ratings)
        self.file_size = file_size

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, розмір файлу: {self.file_size} МБ"

ebook1 = Ebook("Python для всіх", "Чарльз Северенс", [5, 5, 4, 5], 2.5)
print(ebook1)
print("Рейтинги > 4.5:", ebook1.ratings_greater_than(4.5))

class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def library_average_rating(self):
        total_ratings = []
        for book in self.books:
            total_ratings.extend(book.ratings)
        return sum(total_ratings) / len(total_ratings) if total_ratings else 0

    def top_rated_book(self):
        if not self.books:
            return None
        return max(self.books, key=lambda book: book.average_rating())

library = Library("Центральна бібліотека")
library.add_book(book1)
library.add_book(ebook1)

print(f"\nБібліотека: {library.library_name}")
print(f"Середній рейтинг книг: {library.library_average_rating():.2f}")
print("Книга з найвищим рейтингом:")
print(library.top_rated_book())