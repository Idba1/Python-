number = 0
while number < 10:
    number = number + 1
    if number % 2 == 0:
        continue
    print(number)


number = 97
while number < 100:
    number = number + 1
    if number % 2 == 1:
        continue
    print(number)

print("hello")


# MODULE CODE
# odd number ==> after dividing by 2, the remainder will be 1
# even number ==> after dividing by 2, the remainder will be 0


num = 7
while num <= 20:
    num = num + 1
    if num % 2 == 1:
        continue
    print(num)
