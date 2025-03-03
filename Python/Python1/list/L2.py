my_list = [3, 8, 1, 6, 0, 8, 4]
print(my_list)
# Output: 1
print("Index Number of 8-->", my_list.index(8))

# Output: 2
print("Number of 8 in given list-->", my_list.count(8))

my_list.sort()

# Output: [0, 1, 3, 4, 6, 8, 8]
print(my_list)

my_list.reverse()

# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list)

my_list.append(7)
print(my_list)
my_list.extend([9, 11, 13, 1, 3, 5, 42])
print(my_list)