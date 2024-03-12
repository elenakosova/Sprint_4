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

        # проверяем, что добавилось именно две книги
        # получаем текущий словарь с книгами и проверяем его длину
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_max_length(self):
        collector = BooksCollector()

        # Добавляем книгу с максимальной длиной названия
        collector.add_new_book('A' * 40)

        # Проверяем, что добавилась только одна книга
        assert len(collector.get_books_genre()) == 1



    def test_set_book_genre_non_existing_genre(self):
        collector = BooksCollector()

        # Пытаемся установить несуществующий жанр для книги
        collector.set_book_genre('Сияние', 'Драма')

        # Получаем текущий жанр книги (None)
        current_genre = collector.get_book_genre('Сияние')

        # Проверяем, что жанр для книги остался неизменным (равен None)
        assert current_genre == None



    @pytest.mark.parametrize(
        'name, expected_genre',
        [
            ('Ветра зимы','Фантастика'),
            ('Оно','Ужасы')
        ]
    )
    def test_get_book_genre(self, name, expected_genre):
        collector = BooksCollector()

        collector.add_new_book("Ветра зимы")
        collector.add_new_book("Оно")

        # Устанавливаем жанр для книги
        collector.set_book_genre('Ветра зимы', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')

        current_genre = collector.get_book_genre(name)

        # Получаем жанр книги и сравниваем его с ожидаемым результатом
        assert current_genre == expected_genre



    @pytest.mark.parametrize(
        'genre, expected_books',
        [
            ('Фантастика', ["Гарри Поттер и Тайная комната"]),
            ('Ужасы', ["Оно"]),
        ]
    )
    def test_get_books_with_specific_genre(self, genre, expected_books):
        collector = BooksCollector()

        # Добавляем книги и устанавливаем им жанры
        collector.add_new_book("Гарри Поттер и Тайная комната")
        collector.add_new_book("Оно")
        collector.set_book_genre("Гарри Поттер и Тайная комната", "Фантастика")
        collector.set_book_genre("Оно", "Ужасы")

        # Получаем список книг с определенным жанром и сравниваем его с ожидаемым результатом
        assert collector.get_books_with_specific_genre(genre) == expected_books


    def test_get_books_genre(self):
        collector = BooksCollector()

        dictionary = {
            'Гарри Поттер и Философский Камень': 'Фантастика',
            '1984': 'Ужасы',
            'Мастер и Маргарита': 'Ужасы'
        }

        # Добавляем несколько книг с их жанрами
        collector.add_new_book('Гарри Поттер и Философский Камень')
        collector.set_book_genre('Гарри Поттер и Философский Камень', 'Фантастика')

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Ужасы')

        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_genre('Мастер и Маргарита', 'Ужасы')

        # Получаем словарь с книгами и их жанрами
        books_genre = collector.get_books_genre()

        # Проверяем, что словарь содержит ожидаемые значения
        assert books_genre == dictionary





    def test_get_books_for_children_non_children_book(self):
        collector = BooksCollector()

        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Ужасы')
        children_books = collector.get_books_for_children()

        assert '1984' not in children_books



    @pytest.mark.parametrize("book_titles, expected_favorites", [
        (['Гарри Поттер и Тайная комната', '1984'], ['Гарри Поттер и Тайная комната', '1984']),
        (['1984', '1984'], ['1984']),  # Проверяем, что повторное добавление в избранное не изменяет список
        (['Гарри Поттер и Тайная комната'], ['Гарри Поттер и Тайная комната'])
    ])
    def test_add_book_in_favorites(self, book_titles, expected_favorites):
        collector = BooksCollector()

        # Добавляем книги в избранное
        for title in book_titles:
            collector.add_new_book(title)
            collector.add_book_in_favorites(title)

        # Проверяем, что список избранных книг соответствует ожидаемому
        assert collector.get_list_of_favorites_books() == expected_favorites



    @pytest.mark.parametrize("initial_favorites, book_to_delete, expected_favorites", [
        (['Гарри Поттер и Тайная комната', '1984'], 'Гарри Поттер и Тайная комната', ['1984']),
        (['1984', '1984'], 'Несуществующая Книга', ['1984'])
        # Проверяем, что удаление несуществующей книги из избранного не изменяет список
    ])
    def test_delete_book_from_favorites(self, initial_favorites, book_to_delete, expected_favorites):
        collector = BooksCollector()

        # Добавляем книги в избранное
        for book_title in initial_favorites:
            collector.add_new_book(book_title)
            collector.add_book_in_favorites(book_title)

        # Удаляем книгу из избранного
        collector.delete_book_from_favorites(book_to_delete)

        # Проверяем, что список избранных книг соответствует ожидаемому результату
        assert collector.get_list_of_favorites_books() == expected_favorites

    @pytest.mark.parametrize("initial_favorites, modified_favorites", [
        (['Гарри Поттер и Философский Камень', '1984'], ['Гарри Поттер и Философский Камень', '1984']),
        (['Гарри Поттер и Философский Камень', '1984'], ['1984']) # Проверяем, что изменение списка избранных не влияет на результат
    ])
    def test_get_list_of_favorites_books(self, initial_favorites, modified_favorites):
        collector = BooksCollector()

        # Добавляем книги в избранное
        for book_title in initial_favorites:
            collector.add_new_book(book_title)
            collector.add_book_in_favorites(book_title)

        # Проверяем, что список избранных книг соответствует ожидаемому результату
        assert collector.get_list_of_favorites_books() == initial_favorites

        # Модифицируем список избранных книг
        for book_title in modified_favorites:
            collector.delete_book_from_favorites(book_title)

        # Получаем список избранных книг после модификации
        modified_favorites_set = set(modified_favorites)
        updated_favorites_set = set(initial_favorites) - modified_favorites_set
        updated_favorites = list(updated_favorites_set)

        # Проверяем, что изменение списка избранных книг не влияет на результат
        assert collector.get_list_of_favorites_books() == updated_favorites