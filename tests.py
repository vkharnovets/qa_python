import pytest
from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_same_book_twice(self, collector):
        collector.add_new_book('book1')
        collector.add_new_book('book1')

        assert len(collector.get_books_rating()) == 1

    def test_add_new_book_default_rating_is_one(self, collector):
        collector.add_new_book('book1')
        assert collector.get_book_rating('book1') == 1

    def test_set_book_rating_for_nonexistent_book(self, collector):
        collector.set_book_rating('book1', 3)

        assert len(collector.get_books_rating()) == 0

    @pytest.mark.parametrize('rating', [1, 10])
    def test_set_book_rating_valid_value(self, collector, rating):
        book_name = 'book1'
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, rating)

        assert collector.get_book_rating(book_name) == rating

    @pytest.mark.parametrize('rating', [-1, 0, 11])
    def test_set_book_rating_invalid_value(self, collector, rating):
        book_name = 'book1'
        collector.add_new_book(book_name)
        collector.set_book_rating(book_name, rating)

        assert collector.get_book_rating(book_name) == 1

    def test_get_book_rating_for_nonexistent_book(self, collector):
        assert collector.get_book_rating('book1') is None

    def test_get_books_with_specific_rating_get_two_of_three(self, collector):
        collector.add_new_book('book1')
        collector.set_book_rating('book1', 1)

        collector.add_new_book('book2')
        collector.set_book_rating('book2', 2)

        collector.add_new_book('book3')
        collector.set_book_rating('book3', 2)

        assert len(collector.get_books_with_specific_rating(2)) == 2

    def test_add_book_in_favorites_add_two_books(self, collector):
        collector.add_new_book('book1')
        collector.add_book_in_favorites('book1')

        collector.add_new_book('book2')
        collector.add_book_in_favorites('book2')

        assert len(collector.get_list_of_favorites_books()) == 2

    def test_add_book_in_favorites_not_added_to_rating(self, collector):
        collector.add_book_in_favorites('book1')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites(self, collector):
        book_name = 'book1'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)

        assert len(collector.get_list_of_favorites_books()) == 0