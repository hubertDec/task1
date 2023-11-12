from unittest import TestCase
from project.books.views import validate_book_data
from project.customers.views import validate_customer_data
from parameterized import parameterized

class TestXSSPrevention(TestCase):

    @parameterized.expand([("1984", "George Orwell"),
                           ("Book 1", "Author"),
                           ("Practical Iot Hacking", "Chatzis Stais")])
    def test_correct_book_data(self, book_name: str, book_author: str):
            result = validate_book_data(book_name, book_author)
            self.assertEqual(result, True)


    @parameterized.expand([("1984</", "George ]"),
                           ("<script>alert(1)</script>", "Author 1"),
                           ("Pentesting Basics", "onload=http://10.231.1.1")])
    def test_incorrect_book_data(self, book_name: str, book_author: str):
            result = validate_book_data(book_name, book_author)
            self.assertEqual(result, False)


    @parameterized.expand([("marcin kabacki", "Warszawa"),
                           ("John Smith", "New York City"),
                           ("Akira Toriyama", "Tokyo")])
    def test_correct_customer_data(self, customer_name: str, city: str):
            result = validate_customer_data(customer_name, city)
            self.assertEqual(result, True)


    @parameterized.expand([("Marcin</", "Warszawa ]"),
                           ("<script>alert(1)</script>", "Los Angeles"),
                           ("Walter Benedict", "onload=http://10.231.1.1")])
    def test_incorrect_customer_data(self, customer_name: str, city: str):
            result = validate_customer_data(customer_name, city)
            self.assertEqual(result, False)