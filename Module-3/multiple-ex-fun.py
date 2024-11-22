def add(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum


add(23, 23)


def multiply(num1, num2):
    mul = num1 * num2
    return mul


result_mul = multiply(2, 2)
print(result_mul)


def sub(num1, num2):
    sub = num1 - num2
    return sub


result_sub = sub(5, 1)

final_number = add(result_mul, result_sub)
print(final_number)
