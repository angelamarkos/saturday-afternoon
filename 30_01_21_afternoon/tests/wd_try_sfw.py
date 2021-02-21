import unittest
from main import hello
from main import Book

TEST_DICT = {'Raven*Edgar allan poe': ['Raven', 'Edgar allan poe', 'Jan 01 1900']
,'Raven2*Edgar allan poe2': ['Raven2', 'Edgar allan poe2', 'Jan 01 1900'],
'Raven3*Edgar allan poe3': ['Raven3', 'Edgar allan poe3', 'Jan 01 1900']}

class BookT(unittest.TestCase):
    def setUp(self) -> None:
        self.book = Book('Raven', 'Edgar allan poe', 'Jan 01 1900')

    def test_to_string(self):
        for excpected_value, book_args in TEST_DICT.items():
            self.assertEqual(Book(*book_args).to_string(), excpected_value, 'Wrong formatting')

    def tearDown(self) -> None:
        del self.book

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), 'Hello', 'wrong message')



