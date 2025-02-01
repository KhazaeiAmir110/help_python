import unittest

from test_simple import one


class TestOne(unittest.TestCase):
    def test_add(self):
        self.assertEqual(one.add(1, 2), 3)
        self.assertEqual(one.add(10, -10), 0)

    def test_subtract(self):
        self.assertEqual(one.subtract(1, 2), -1)
        self.assertEqual(one.subtract(10, -10), 20)

    def test_multiply(self):
        self.assertEqual(one.multiply(1, 2), 2)
        self.assertEqual(one.multiply(10, 0), 0)

    def test_divide(self):
        self.assertEqual(one.divide(2, 2), 1)


if __name__ == '__main__':
    unittest.main()
