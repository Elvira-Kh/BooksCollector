
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
        assert collector.get_books_genre() == {'Новая книга': ''}

    #проверяем невозможность добавить две книги с одиноковым именем
    def test_add_new_book_two_books_with_same_name(self, collector):
            collector.add_new_book('Унесенные ветром')
            collector.add_new_book('Война и Мир')
            assert collector.books_genre == {'Унесенные ветром': '', 'Война и Мир': ''}

    #Проверяем возможность установить жанр
    @pytest.mark.parametrize("name, genre", [('Молчание ягнят', 'Триллеры')])
    def test_set_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Молчание ягнят')
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre('Молчание ягнят') == genre

    #Проверяем добавление нового жанра
    @pytest.mark.parametrize('genre',['Фантастика','Комедии'])
    def test_get_books_with_specific_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Трон')
        collector.add_new_book('Бриджет Джонс')
        collector.set_book_genre('Трон','Фантастика')
        collector.set_book_genre('Бриджет Джонс', 'Комедии')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Трон']

    #проверка если жанр не установлен (genre = None)
    @pytest.mark.parametrize('name, genre', [('Трое в лодке', None)])
    def test_get_book_genre_no_specific_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre[name] == genre

    #есть жанр книги но нет имени (name = None)
    @pytest.mark.parametrize('genre', ['Фантастика'])
    def test_get_book_genre_with_missing_name(self,genre):
        collector: BooksCollector = BooksCollector()
        collector.add_new_book('Я-Робот')
        book_name = None
        self.genre = 'Фантастика'
        self.genre = collector.get_book_genre(book_name)

    #Проверяем, что список книг для детей пуст
    @pytest.mark.parametrize('books_genre, expected_length', [
        ({
             'Книга 1': 'Ужасы',
             'Книга 2': 'Детективы',
             'Книга 3': 'Фантастика'
         }, 0),
    ])
    def test_get_books_for_children(books_collector, books_genre, expected_length):
        books_collector = BooksCollector()
        books_collector.books_genre = books_genre
        books_for_children = books_collector.get_books_for_children()
        assert len(books_for_children) == expected_length

    #Проверяем, что книга добавляется в Избранное
    @pytest.fixture
    def favorites():
        return ['Что делать, если ваш кот хочет вас убить']

    @pytest.mark.parametrize('name', ['Что делать, если ваш кот хочет вас убить'])
    def test_add_book_in_favorites(books_collector, favorites, name):
            books_collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
            assert 'Что делать, если ваш кот хочет вас убить' in books_collector.favorites
            assert books_collector.get_list_of_favorites_books() == favorites

    #Проверяем, что книга удаляется из Избранного
    @pytest.mark.parametrize('name', ['Что делать, если ваш кот хочет вас убить', 'Гордость и предубеждение и зомби'])
    def test_delete_book_from_favorites(books_collector, name):
        books_collector.favorites = ['Что делать, если ваш кот хочет вас убить']

    def delete_book_from_favorites(books_collector, name):
        books_collector.favorites.remove(name)

    books_collector.delete_book_from_favorites(name)
    assert name not in books_collector.favorites

    #Проверяем получение списка Избранных книг
    def test_get_list_of_favorites_books(self, books_collector):
        books_collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        favorites = books_collector.get_list_of_favorites_books()








