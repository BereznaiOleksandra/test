from faker import Faker

from main import Book, Author

from polyfactory.factories import DataclassFactory


class BookFactory(DataclassFactory[Book]):
    __model__ = Book

    @classmethod
    def title(cls):
        return Faker().sentence(nb_words=3)

    @classmethod
    def year(cls):
        return int(Faker().year())

    @classmethod
    def isbn(cls):
        return Faker().isbn10()

    @classmethod
    def price(cls):
        return Faker().random_number(digits=2, fix_len=False)


class AuthorFactory(DataclassFactory[Author]):
    __model__ = Author

    @classmethod
    def full_name(cls):
        return Faker().name()

    @classmethod
    def bio(cls):
        return Faker().sentence(nb_words=10)

    @classmethod
    def book_list(cls):
        return [BookFactory.build()]
