numbers = [12, 23, 4, 534, 63, 63, 23, 234, 35, 354]
# numbers_iter = iter(numbers)
# print(sorted(list(numbers_iter)))
# numbers_iter = iter(numbers)
# print(list(numbers_iter))

numbers_iter = iter(numbers)
print(next(numbers_iter))

try:
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print("hello from iterator world!")
    print(next(numbers_iter))
    print(next(numbers_iter))
    print("i'm doing something!")
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
    print("i think finished")
    print(next(numbers_iter))
    print(next(numbers_iter))
    print(next(numbers_iter))
except StopIteration:
    print("iter stopped")
