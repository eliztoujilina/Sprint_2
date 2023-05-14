import pytest

from main import BooksCollector


class TestAddBook:
    def test_add_new_book(self):
        book_name = 'Гарри Поттер'
        books_collector = BooksCollector()
        books_collector.add_new_book(book_name)
        assert book_name in books_collector.books_rating.keys()
        assert books_collector.get_book_rating(book_name)


    def test_add_existing_book(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Гарри Поттер')
        books_collector.add_new_book('Гарри Поттер')
        assert len(books_collector.books_rating) == 1

    def test_set_book_rating_invalid_name(self):
        books_collector = BooksCollector()
        books_collector.set_book_rating('Сумерки', 7)
        assert books_collector.books_rating.get('Сумерки') is None

    def test_set_book_rating_out_of_range(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Сумерки')
        books_collector.add_new_book('Гарри Поттер')
        books_collector.set_book_rating('Сумерки', -1)
        assert books_collector.get_book_rating('Сумерки') == 1

        books_collector.set_book_rating('Гарри Поттер', 11)
        assert books_collector.get_book_rating('Гарри Поттер') == 1

    def test_get_book_rating_invalid_name(self):
        books_collector = BooksCollector()
        assert books_collector.get_book_rating('Гарри Поттер') is None

    def test_add_book_in_favorites(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Алиса в стране чудес')
        books_collector.add_book_in_favorites('Алиса в стране чудес')
        assert 'Алиса в стране чудес' in books_collector.favorites

    def test_not_existing_book_to_favorite(self):
        books_collector = BooksCollector()
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert len(books_collector.favorites) == 0

    def test_delete_book_from_favorites(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Алиса в стране чудес')
        books_collector.add_book_in_favorites('Алиса в стране чудес')
        books_collector.delete_book_from_favorites('Алиса в стране чудес')
        assert 'Алиса в стране чудес' not in books_collector.favorites

    def test_get_list_of_favorites_books(self):
        books_collector = BooksCollector()
        books_collector.add_new_book('Гарри Поттер')
        books_collector.add_new_book('Алиса в стране чудес')
        books_collector.add_book_in_favorites('Гарри Поттер')
        books_collector.add_book_in_favorites('Алиса в стране чудес')
        assert books_collector.get_list_of_favorites_books() == ['Гарри Поттер', 'Алиса в стране чудес']