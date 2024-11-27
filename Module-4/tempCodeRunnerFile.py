numbers = [12, 23, 4, 534, 63, 63, 23, 234, 35, 354]


def get_numbers(num):
    for num in get_numbers:
        yield num


result = get_numbers(numbers)
print(next(result))
