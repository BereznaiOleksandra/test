from faker import Faker
from polyfactory.factories import DataclassFactory

from app.main import Author, Book, BookZeroDiscount


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

    @classmethod
    def discount(cls):
        return BookZeroDiscount()


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
