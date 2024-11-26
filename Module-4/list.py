numbers = [12, 23, 4, 534, 6345, 23, 234, 32, 354]

print(numbers[8])  # index 0,1,2,3,4,5,6,7
print(numbers[-1])  # index -1,-2,-3,-4,-5,-6,-7,-8,-9

# list [numbers[start:end:step]]
print(numbers[3:5])  # slice. for this instruction it will be taken 3rd and 4th value.
print(numbers[3:-5])
print(numbers[0:9:2])
print(numbers[4:0:-1])  # reverse
print(numbers[:])  # print full array
print(numbers[::-1])  # full array reverse

numbers.append(334)
print(numbers[:])
numbers.pop()
print(numbers[:])
numbers.sort()  # sort
print(numbers[:])

numbers.remove(4)
print(numbers[:])

numbers.insert(0, 122)
print(numbers[:])
count = numbers.count(23)
print(count)
