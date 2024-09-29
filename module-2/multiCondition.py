# examMark = input("enter your exam mark: ")
# iExamMark = int(examMark)
# if iExamMark >= 40 and iExamMark <= 100:
#     print("you passed")
# elif iExamMark < 40 and iExamMark >= 0:
#     print("Failed")
# else:
#     print("enter a valid mark")


device = "laptop"
device2 = "tablet"

if device == "laptop" or device2 == "computer":
    print("you can start programming")
else:
    print("you need to buy laptop or desktop computer")


if device == "laptop" and device2 == "computer":
    print("you can start programming")
else:
    print("you need to buy laptop or desktop computer")