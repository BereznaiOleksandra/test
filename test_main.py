import datetime

from factory import BookFactory, AuthorFactory


def test_add_book():
    book = BookFactory.build()
    author = AuthorFactory.build()
    author.add_book(book)
    assert book in author.get_book_list()


def test_age_of_book():
    book = BookFactory.build(year=2020)
    assert book.age_of_book() == 5


def test_book_older_than_5_years():
    year = datetime.datetime.now().year - 6
    book = BookFactory.build(year=year)
    author = AuthorFactory.build()
    author.add_book(book)
    assert author.book_list[-1].age_of_book() > 5

def test_book_younger_than_5_years():
    year = datetime.datetime.now().year - 4
    book = BookFactory.build(year=year)
    author = AuthorFactory.build()
    author.add_book(book)
    assert author.book_list[-1].age_of_book() < 5
