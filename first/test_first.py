from unittest import TestCase

from first import first


class FirstTest(TestCase):
    def test_many(self):
        self.assertEqual(first(x for x in range(20)), 0)

    def test_one(self):
        self.assertEqual(first([0]), 0)

    def test_default(self):
        self.assertEqual(first([], 'dee'), 'dee')

    def test_empty(self):
        try:
            first([])
        except ValueError:
            return ValueError
