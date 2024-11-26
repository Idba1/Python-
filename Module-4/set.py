numbers = [12, 23, 4, 534, 63, 63, 23, 234, 32, 354]
print(numbers)

# set
# nums = {12, 23, 4, 534, 63, 63, 23, 234, 32, 354}
# print(nums)

numbers_set = set(numbers)
print(numbers_set)
numbers_set.add(4)  # 4 will be not added. cz 4 already exist in this set
numbers_set.add(78)
print(numbers_set)
numbers_set.remove(4)
print(numbers_set)
print(len(numbers_set))
numbers_set.add(98)
numbers_set.add(38)
print(len(numbers_set))
