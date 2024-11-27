numbers = [12, 23, 4, 534, 63, 63, 23, 234, 35, 354]
total = sum(numbers)
print(total)

total = 0
print(total)
for num in numbers:
    total = total + num

print(total)

total = 0
print(total)
nums = {12, 23, 2, 534, 64, 63, 24, 234, 35, 354}
for n in nums:
    total = total + n
print(total)

total = 0
print(total)
tuple_nums = 12, 23, 2, 534, 64, 63, 24, 234, 35, 354
for num in tuple_nums:
    total = total + num
print(total)

total = 0
print(total)
marks = {"phy": 14, "che": 98, "bio": 34}
for mark in marks:
    value = marks[mark]
    print(mark, value)
    total = total + value
print(total)
