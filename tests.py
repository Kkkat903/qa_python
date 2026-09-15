import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_more_than_40_symbols(self):
        collector = BooksCollector()

        book = "А" * 67
        collector.add_new_book(book)

        assert book not in collector.books_genre

    @pytest.mark.parametrize("book, genre", [("Мастер и Маргарита", "Фантастика"), ("Лес", "Ужасы"), ("Все красное", "Комедии")])
    def test_set_book_genre(self, book, genre):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Лирика")

        assert collector.get_book_genre("Мастер и Маргарита") == ""

    def test_get_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")

        assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Мастер и Маргарита")
        collector.add_new_book("Сто лет одиночества")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        collector.set_book_genre("Сто лет одиночества", "Фантастика")

        result = collector.get_books_with_specific_genre("Фантастика")

        assert result == ["Мастер и Маргарита", "Сто лет одиночества"]
                          
    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Мастер и Маргарита")

        assert collector.get_books_genre() == {"Мастер и Маргарита": ""}

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book("Мастер и Маргарита")
        collector.add_new_book("Белая гвардия")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        collector.set_book_genre("Лес", "Ужасы")

        result = collector.get_books_for_children()

        assert result == ["Мастер и Маргарита"]

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book = "Мастер и Маргарита"

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        assert book in collector.favorites

    def test_add_book_in_favorites_not_existing_book(self):
        collector = BooksCollector()

        collector.add_book_in_favorites("Мастер и Маргарита")

        assert collector.favorites == []

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book = "Мастер и Маргарита"

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)

        assert collector.favorites == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        book = "Мастер и Маргарита"

        collector.add_new_book(book)
        collector.add_book_in_favorites(book)

        result = collector.get_list_of_favorites_books()

        assert result == [book]


