nums = []

while True:
    n = input()
    if n == '0': break
    nums.insert(0, n)

print('\n'.join(nums))
