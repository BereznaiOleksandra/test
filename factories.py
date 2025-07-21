from faker import Faker
from polyfactory.factories import DataclassFactory
from polyfactory.factories.pydantic_factory import ModelFactory

from app.main import Author, AuthorDTO, Book, BookDTO, BookZeroDiscount, CatalogDTO


class BookFactory(DataclassFactory[Book]):
    __model__ = Book

    @classmethod
    def title(cls) -> str:
        return Faker().sentence(nb_words=3)

    @classmethod
    def year(cls) -> int:
        return int(Faker().year())

    @classmethod
    def isbn(cls) -> str:
        return Faker().isbn10()

    @classmethod
    def price(cls) -> int:
        return Faker().random_number(digits=2, fix_len=False)

    @classmethod
    def discount(cls) -> BookZeroDiscount:
        return BookZeroDiscount()


class AuthorFactory(DataclassFactory[Author]):
    __model__ = Author

    @classmethod
    def full_name(cls) -> str:
        return Faker().name()

    @classmethod
    def bio(cls) -> str:
        return Faker().sentence(nb_words=10)

    @classmethod
    def book_list(cls) -> list[Book]:
        return [BookFactory.build()]


class AuthorDTOFactory(ModelFactory[AuthorDTO]):
    __model__ = AuthorDTO

    @classmethod
    def id(cls) -> int:
        return Faker().random_number()

    @classmethod
    def full_name(cls) -> str:
        return Faker().name()

    @classmethod
    def bio(cls) -> str:
        return Faker().sentence(nb_words=10)


class BookDTOFactory(ModelFactory[BookDTO]):
    __model__ = BookDTO

    @classmethod
    def isbn(cls) -> str:
        return str(Faker().random_number(digits=13, fix_len=True))

    @classmethod
    def title(cls) -> str:
        return Faker().sentence(nb_words=3)

    @classmethod
    def year(cls) -> int:
        return int(Faker().year())

    @classmethod
    def price(cls) -> float:
        return Faker().random_number(digits=2, fix_len=False)

    @classmethod
    def authorId(cls) -> int:
        return Faker().random_number()


class CatalogDTOFactory(ModelFactory[CatalogDTO]):
    __model__ = CatalogDTO

    @classmethod
    def books(cls) -> list[BookDTO]:
        return [BookDTOFactory.build()]

    @classmethod
    def authors(cls) -> list[AuthorDTO]:
        return [AuthorDTOFactory.build()]


catalog = CatalogDTOFactory.build()
print(catalog)
