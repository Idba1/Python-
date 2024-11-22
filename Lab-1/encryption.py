data = input("data: ")
shift = int(input("shift: "))
output = ""

for character in data:
    output += chr((ord(character) + shift - 97) % 26 + 97)
print(output)
