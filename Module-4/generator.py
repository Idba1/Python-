numbers = [12, 23, 4, 534, 63, 63, 23, 234, 35, 354]


def get_numbers(nums):
    for num in nums:
        yield num


result = get_numbers(numbers)
try:
    print(next(result))
    print(next(result))
    print(next(result))
    print("hello from generator world!")
    print(next(result))
    print(next(result))
    print("i'm doing something!")
    print(next(result))
    print(next(result))
    print(next(result))
    print(next(result))
    print("i think finished")
    print(next(result))
    print(next(result))
    print(next(result))
except:
    print("generator stopped")
