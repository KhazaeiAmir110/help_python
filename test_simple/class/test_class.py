import unittest

from class_model import Person


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.person1 = Person("amir", "amiri")
        self.person2 = Person("ali", "alibaba")

    def test_full_name(self):
        self.assertEqual(self.person1.full_name(), "amir amiri")
        self.assertEqual(self.person2.full_name(), "ali alibaba")

    def test_email(self):
        self.assertEqual(self.person1.email(), "amiramiri@gmail.com")
        self.assertEqual(self.person2.email(), "alialibaba@gmail.com")
