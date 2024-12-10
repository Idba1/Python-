def add(a, b):
    sum = a + b
    # print(sum)
    return sum


def deduct(x, y):
    sub = x - y
    return sub


sum = add(1, 2)
sub = deduct(9, 3)
# print(sub)


class Phone:
    color = "black"
    features = ["camera", "waterproof", "can be use as a hammer"]

    def call(self):
        print("ring ring ring........")

    def send_sms(self, text, phn):
        sms = f"Sending message: {text}!\nTo: {phn}"
        return sms


my_phone = Phone()
my_phone.call()
sms = my_phone.send_sms("i missed to miss you", "0178219")
print(sms)
