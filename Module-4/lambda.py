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
