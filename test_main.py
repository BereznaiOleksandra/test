from main import Book, Author
import unittest
from unittest import TestCase

class TestMain(TestCase):

    def test_book_younger_5_years_old_exist(self):
        self.book1 = Book("Book1", 2019, "1234567890123", 30.4)
        self.book2 = Book("Book2", 2022, "1534567890123", 20.4)
        self.author = Author("Jack Nikon", "Good writer", [])
        self.author.add_book(self.book1)
        self.author.add_book(self.book2)
        result = False
        for book in self.author.book_list:
            if book.age_of_book() < 5:
                result = True
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
