class Phone:
    manufactured = "china"

    def __init__(self, brand, color, price):
        self.brand = brand
        self.color = color
        self.price = price

    def send_sms(self, number, text):
        sms = f"sending: {text} to: {number}"
        return sms


myPhone = Phone("Iphone", "deep blue", 190000)
print(myPhone.brand, myPhone.manufactured)
print(myPhone.color)

brotherPhone = Phone("samsung", "pink", 230000)
print(brotherPhone.brand)
print(brotherPhone.color)
