
import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже

    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #проверяем возможность добавить книгу
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('Новая книга')
        assert collector.get_book_genre('Новая книга') == ''


    #Проверяем возможность установить жанр
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Молчание ягнят')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Молчание ягнят', 'Детективы')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Молчание ягнят') == 'Детективы'
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    #Проверяем добавление нового жанра
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Трон')
        collector.add_new_book('Бриджет Джонс')
        collector.set_book_genre('Трон', 'Фантастика')
        collector.set_book_genre('Бриджет Джонс', 'Комедии')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert books == ['Трон']

    #проверка получения жанра
    @pytest.mark.parametrize("books_genre, expected_result", [
        ({"Фантастика": ["Мандалорец", "Трон"], "Ужасы": ["Оно", "Противостояние"]},
         {"Фантастика": ["Мандалорец", "Трон"], "Ужасы": ["Оно", "Противостояние"]}),
        ({}, {})
    ])

    def test_get_books_genre(self, books_genre, expected_result):
        collector = BooksCollector()
        collector.books_genre = books_genre
        result = collector.get_books_genre()
        assert result == expected_result

    #есть жанр книги но нет имени (name = None)
    @pytest.mark.parametrize('genre', ['Фантастика', 'Детективы'])
    def test_get_book_genre_with_missing_name(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Я-Робот')
        book_name = 'Я-Робот'
        collector.set_book_genre('Я-Робот', genre)
        book_genre = collector.get_book_genre(book_name)
        assert book_genre == genre

    #Проверяем, что список книг для детей пуст
    @pytest.mark.parametrize('books_genre, expected_length', [
        ({
             'Книга 1': 'Ужасы',
             'Книга 2': 'Детективы',
             'Книга 3': 'Фантастика'
         }, 1),
    ])
    def test_get_books_for_children(self, books_genre, expected_length):
        collector = BooksCollector()
        collector.books_genre = books_genre
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == expected_length

    #Проверяем, что книга добавляется в Избранное
    @pytest.mark.parametrize("name", [
        ('Что делать, если ваш кот хочет вас убить'),
        ('Гордость и предубеждение и зомби'),
        ('Мандалорец')
    ])
    def test_add_book_in_favorites(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites
        assert collector.get_list_of_favorites_books() == [name]

        #Проверяем, что книга удаляется из Избранного
    @pytest.mark.parametrize('name', ['Что делать, если ваш кот хочет вас убить'])
    def test_delete_book_from_favorites(self, name):
        collector = BooksCollector()
        collector.favorites = ['Что делать, если ваш кот хочет вас убить']
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
        assert name not in collector.favorites

    #Проверяем получение списка Избранных книг
    def get_list_of_favorites_books(self):
        return self.favorites









