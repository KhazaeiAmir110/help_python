from first import add

from keeping_result import full_name

add_ = add.signature((33, 67))

name_ = full_name.signature(("amir", "khazaei"))

add_.delay()
name_.delay()

# result = add.apply_async((4, 5), link=full_name.signature(("amir", "khazaei")))
