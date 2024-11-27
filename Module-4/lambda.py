def square(x):
    return x * x


print(square(2))
print("end\n")

# this function in one line
square = lambda x: x * x
print(square(2))

add = lambda x, y: x + y
print(add(1, 3))

numbers = [12, 23, 4, 534, 63, 63, 23, 234, 35, 354]
doubled_it = lambda x: x * 2
doubleList = []
print(doubled_it(8))
for num in numbers:
    double = doubled_it(num)
    print(double)
    doubleList.append(double)
print(numbers)
print(doubleList)

# module
numbers = [12, 23, 4, 534, 63, 63, 23, 234, 35, 354]
doubled_it = lambda x: x * 2
doubled_it2 = map(doubled_it, numbers)
print(numbers)
print(list(doubled_it2))

# in shortcut
doubled_num = map(lambda x: x * 2, numbers)
print("output for shortcut-->", list(doubled_num))


# filter
numbers = [0, -12, -45, 100, 12, 23, 4, 534, 63, 63, 23, 234, 35, 354]
bigger_numbers = filter(lambda num: num >= 100, numbers)
print(list(bigger_numbers))
lower_numbers = filter(lambda num: num < 100 and num >= 0, numbers)
print(list(lower_numbers))
negative_numbers = filter(lambda num: num < 0, numbers)
print(list(negative_numbers))
even_numbers = filter(lambda num: num % 2 == 0 and num > 0, numbers)
print(list(even_numbers))
odd_numbers = filter(lambda num: num % 2 == 1 and num > 0, numbers)
print(list(odd_numbers))
