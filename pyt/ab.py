my_list = [3, 8, 1, 6, 0, 8, 4]
print(my_list)
print("Index Number of 8-->", my_list.index(8))
print("Number of 8 in given list-->", my_list.count(8))
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
my_list.append(7)
print(my_list)
my_list.extend([9, 11, 13, 1, 3, 5, 42])
print(my_list)
print(my_list[0])
my_list[0] = 1
print(my_list[0])
my_list[1:4] = [3, 5, 7]
print(my_list)
