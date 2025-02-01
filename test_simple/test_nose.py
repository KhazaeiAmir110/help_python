from test_simple import one


def test_add(self):
    assert one.add(1, 2) == 3
    assert one.add(10, -10) == 0


def test_subtract(self):
    assert one.subtract(1, 2) == -1
    assert one.subtract(10, -10) == 20


def test_multiply(self):
    assert one.multiply(1, 2) != 10
    assert one.multiply(10, 0) == 0


def test_divide(self):
    assert one.divide(2, 2) == 1

# nosetests test_nose.py
