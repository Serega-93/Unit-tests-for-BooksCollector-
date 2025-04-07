import pytest

from data import BOOK_NAME, GENRE
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    # проверяем добавление книг с количеством содержания символов на границах
    # допустимого диапазона от 1 до 40
    @pytest.mark.parametrize('values', ['а',# 1 символ
                                      'ааааааааааааааааааааааааааааааааааааааа',# 39 символов
                                      'аааааааааааааааааааааааааааааааааааааааа'])# 40 символов
    def test_add_new_book_check_positive_boundary_values(self, collector, values):
        collector.add_new_book(values)
        book_name = collector.get_books_genre()
        assert  values in book_name

    # проверяем что новой книге устанавливается жанр
    def test_set_book_genre_set_new_book_genre(self, collector):
        collector.add_new_book(BOOK_NAME[0])
        collector.set_book_genre(BOOK_NAME[0], GENRE[0])
        assert collector.get_book_genre(BOOK_NAME[0]) == GENRE[0]

    # проверяем что у добавленной книге нет жанра
    def test_get_book_genre_new_book_not_genre(self, collector):
        collector.add_new_book(BOOK_NAME[0])
        assert collector.get_book_genre(BOOK_NAME[0]) == ''

    # проверяем получение книги по жанру
    def test_get_books_with_specific_genre_get_book_by_genre(self, collector):
        collector.add_new_book(BOOK_NAME[1])
        collector.set_book_genre(BOOK_NAME[1], GENRE[4])
        assert  collector.get_books_with_specific_genre(GENRE[4]) == [BOOK_NAME[1]]

    # проверяем возвращение книг подходящих детям
    def test_get_books_for_children_get_books(self, collector):
        collector.add_new_book(BOOK_NAME[3])
        collector.add_new_book(BOOK_NAME[2])
        collector.set_book_genre(BOOK_NAME[3], GENRE[3])
        collector.set_book_genre(BOOK_NAME[2], GENRE[1])
        assert  collector.get_books_for_children() == [BOOK_NAME[3]]

    # проверяем добавление книги в избранное
    def test_add_book_in_favorites_add_book(self, collector):
        collector.add_new_book(BOOK_NAME[0])
        collector.add_book_in_favorites(BOOK_NAME[0])
        assert collector.get_list_of_favorites_books() == [BOOK_NAME[0]]

    # проверяем удаление книги из избранного
    def test_delete_book_from_favorites_delete_book(self, collector):
        collector.add_new_book(BOOK_NAME[0])
        collector.add_book_in_favorites(BOOK_NAME[0])
        collector.delete_book_from_favorites(BOOK_NAME[0])
        assert collector.get_list_of_favorites_books() == []

    # проверяем что одна и та же книга не добавляется ещё раз
    def test_add_new_book_add_book_again(self, collector):
        collector.add_new_book(BOOK_NAME[0])
        collector.add_new_book(BOOK_NAME[0])
        book_list = collector.get_books_genre()
        assert  len(book_list) == 1





