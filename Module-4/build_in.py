largest = max(12, 23, 4, 534, 63, 63, 23, 234, 35, 354)
print(largest)
smallest = min(12, 23, 4, 534, 63, 63, 23, 234, 35, 354, 0, -21)
print(smallest)

# in set
nums = {12, 23, 4, 534, 63, 63, 23, 234, 35, 354}
big_nums = max(nums)
print(big_nums)

numbers = [12, 23, 4, 534, 63, 63, 23, 234, 35, 354]
reverse_nums = reversed(numbers)
print(list(reverse_nums))

# descending
sorted_num = sorted(numbers, reverse=True)
print(list(sorted_num))
# ascending
sorted_num = sorted(numbers, reverse=False)
print(list(sorted_num))
