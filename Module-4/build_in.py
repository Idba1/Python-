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


# Sorting a dictionary based on values
actors = [
    {"name": "sakib", "age": 34},
    {"name": "rakib", "age": 54},
    {"name": "akib", "age": 24},
    {"name": "korim", "age": 44},
    {"name": "rahim", "age": 74},
]
# sorted_actors = sorted(actors, key=lambda actor: actor["age"], reverse=False)
# print(sorted_actors)
sorted_actors = sorted(actors, key=lambda actor: actor["name"], reverse=False)
print(sorted_actors)

friends = {"rakib", "akib", "sakib", "korim", "rahim"}
sorted_friends = sorted(friends)
print(sorted_friends)
sorted_friends_reverse = sorted(friends, reverse=True)
print(sorted_friends_reverse)
