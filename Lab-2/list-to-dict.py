my_list = ["@F1", "OBCD", "!", "@F2", "ADDAB", "!", "@F3", "OKKA", "!"]

# expected: {"@F1": "OBCD", "@F2": "ADDAB", "@F3": "OKKA"}

output_dict = {}
for index, val in enumerate(my_list):
    if val[0] == "@":
        output_dict[val] = my_list[index + 1]

print(output_dict)
