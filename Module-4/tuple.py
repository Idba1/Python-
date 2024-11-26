numbers = [12, 23, 4, 534, 63]
print(numbers)

# tuple
tuple_nums = 12, 23, 4, 534, 63
print(tuple_nums)
# tuple_nums[2] = 22   #you can't change this value
print(tuple_nums)
print(tuple_nums[2])  # you can access and print value but you will not change this

# in this way tou can change/update this value
tuple_2D = ([12, 32, 42], [213, 213, 213])
print(tuple_2D)
tuple_2D[0][1] = 12
print(tuple_2D)
tuple_2D[0][2] = 12
print(tuple_2D)

tuple_create_from_list = tuple(numbers)
print(tuple_create_from_list)
