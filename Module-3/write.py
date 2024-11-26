# with open("message.txt", "w") as fileWrite:
#     fileWrite.write("second test")


with open("append.txt", "a") as fileWrite:  # append korbe
    fileWrite.write("second test\n")

# read
with open("append.txt", "r") as fileRead:  # read file
    text = fileRead.read()
    print(text)
