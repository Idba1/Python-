number = 13
while number <= 40:
    number = number + 1
    if number==40:
        break
    if number % 2 == 0:
        continue
    print(number)
