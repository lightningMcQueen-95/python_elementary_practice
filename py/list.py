#creating lists
print("****creating lists****")
num=[1,2,3,4]
print("Numbered-->",num)

letter=['a','s','d','f']
print("letter-->",letter)

stg=["Hello", "World"]
print("string-->",stg)

mix=[1,5,"Hello", "World"]
print("mixed-->",mix)

mat=[[1,2],['a','b']]
print("Matrix-->",mat,"\n\n\n")


# Nested List
n_list = ["Happy", [2, 0, 1, 5]]

# Nested indexing
print(n_list[0][1])

print(n_list[1][3])

print("\n""\n""\n")






#accessing elements in lists
print("****Accessing elements in lists****","\n")

print("Forward Indexing is always starts from 0, i.e. 0,1,2,3,4,..... from left to right in a list""\n")

print("Backward indexing is always starts from -1, i.e. -1,-2,-3,-4,..... from right hand side to left hand side in a list""\n")

print("For example consider a list-->",mix,"\n")

print("Now we have to access the nth element form left then we have to write the statement-->(print(list_name[n-1])) for getting desiered result")
print("result-->",mix[2],"\n")

print("Now we have to access the nth element form right then we have to write the statement-->(print(list_name[-n])) for getting desiered result")
print("reult-->",mix[-3],"\n")

print("now we want to print the elemnts till a index then we have to write the statement-->(print(list_name[:n+1])) for getting desiered result")
print("why n+1 because ':' give results till n-1")
print("reult-->",mix[:3],"\n")

print(mix[1:])
print(mix[::2])
print(mix[::-1],"\n\n\n")








#sample list ['p','y','t','h','o','n']
my_list = ['p','y','t','h','o','n']
print("For example our sample list is->",my_list,"\n")

# elements 3rd to 5th
print("elements 3rd to 5th",my_list[2:5],"\n")

# elements beginning to 4th
print("elements beginning to 4th",my_list[:-5],"\n")

# elements 6th to end
print("elements 6th to end",my_list[5:],"\n")

# elements beginning to end
print("elements eginning to end",my_list[:],"\n")

print("\n""\n""\n")









my_list1 = [3, 8, 1, 6, 0, 8, 4]
print("For example our sample list is->",my_list1,"\n")
print(my_list1)
# Output: 1
print("Index Number of 8-->", my_list1.index(8))

# Output: 2
print("Number of 8 counter in given list-->", my_list1.count(8))

#for sorting list in ascending order
my_list1.sort()

# Output: [0, 1, 3, 4, 6, 8, 8]
print(my_list1)

my_list1.reverse()

# Output: [8, 8, 6, 4, 3, 1, 0]
print(my_list1)

#use of append and extend
my_list1.append(7)
print(my_list1)
my_list1.extend([9, 11, 13, 1, 3, 5, 42])
print(my_list1)

print("\n""\n""\n")









#Opertaors in list
x=[0]*100
print(x)

#concatination of two list using +
print(letter)
print(stg)
concat=letter+stg
print(concat)

var=list("Hey There")
print(var)

print(num)
two, one, *other=num
print(two)
print(one)
print(other)

print("\n""\n""\n")



#methods in lists

print(num)
num.append(6)
print(num)

print(stg)
num.extend(stg)
print(num)

num.insert(5,"Namaste")
print(num)

num.remove("Namaste")
print (num)

var1=['q','w','s','h']
var1.sort()
print(var1)

var2=[4,9,6,8,5,1]
var2.sort()
print(var2)

print("\n""\n")






#Buitin function with list
print("Buitin function with list")
x=[4,9,6,8,5,1]
print(len(x))
print(min(x))
print(sum(x))
print(sum(x)/len(x))

print("\n""\n")



#for printting list of n natural number
list1=list(range(1,11))
print(list1)
odd=list1[::2]
print(odd)
even=list1[1::2]
print(even)

