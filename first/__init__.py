list_test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
_market = object()


def first(iterable, default=_market):
    try:
        return next(iter(iterable), default)
    except StopIteration:
        if default is _market:
            raise ValueError("first argument must be an iterable !!!")
        return default


print(first(list_test))
