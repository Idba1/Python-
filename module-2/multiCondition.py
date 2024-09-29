examMark = input("enter your exam mark: ")
iExamMark = int(examMark)
if iExamMark >= 40 and iExamMark <= 100:
    print("you passed")
elif iExamMark < 40 and iExamMark >= 0:
    print("Failed")
else:
    print("enter a valid mark")
