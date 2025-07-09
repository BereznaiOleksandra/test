from main import Book, Author

from polyfactory.factories import DataclassFactory


class BookFactory(DataclassFactory[Book]):
    __model__ = Book


class AuthorFactory(DataclassFactory[Author]):
    __model__ = Author


def test_is_book() -> None:
    book_instance = BookFactory.build()
    assert isinstance(book_instance, Book)
    assert isinstance(book_instance.name, str)
    assert isinstance(book_instance.year, int)
    assert isinstance(book_instance.isbn, str)
    assert isinstance(book_instance.price, float)

def test_is_author() -> None:
    author_instance = AuthorFactory.build()
    assert isinstance(author_instance, Author)
    assert isinstance(author_instance.full_name, str)
    assert isinstance(author_instance.bio, str)
    assert isinstance(author_instance.book_list, list)
