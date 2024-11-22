def add(num1, num2):
    sum = num1 + num2
    print(f"num1: {num1} num2: {num2}", sum)
    return sum


add(23, 27)
add(num2=23, num1=27)


# default value
def add(num1, num2=1):
    sum = num1 + num2
    print(sum)
    return sum


add(23)
add(22, 23)


# tuple
def multiply(*numbers):
    result = 1
    print(numbers)
    for num in numbers:
        result = num * result
    return result


result_mul = multiply(2, 2, 2, 2)
print(result_mul)
