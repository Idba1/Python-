numbers = [12, 23, 4, 534, 63, 63, 23, 234, 35, 354]

odd_num = []
for num in numbers:
    if num % 2 == 1:
        odd_num.append(num)
print(odd_num)

# in shortcut
double_num = [num * 2 for num in numbers]
print(double_num)
odd_num = [num for num in numbers if num % 2 == 1]
print(odd_num)
odd_num2 = [num for num in numbers if num % 2 == 1 and num % 5 == 0]
print(odd_num2)
even_num = [num for num in numbers if num % 2 == 0]
print(even_num)


names = ["sakib", "rakib", "asib", "karib"]
ages = [23, 45, 34, 30]
pairs = [(name, age) for name in names for age in ages if age < 30]
print(pairs)

for name in names:
    print(name)
    for age in ages:
        if age < 30:
            print(name, age)
