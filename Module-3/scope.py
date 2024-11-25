balance = 1000
print(balance)


def price(price, quantity):
    global balance  # use global keyword for value set for global variable
    total = price * quantity
    print(total)
    balance = balance - total
    print(balance)
    return balance


price(20, 10)
print(balance)
