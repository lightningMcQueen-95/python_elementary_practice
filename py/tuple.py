#creataing tuples
emp=()
print(type(emp))
print(emp)

x=("1")
print(type(x))
y=("1",)
print(type(y))

list1=[1,2,3,4]
tuple1=(1,2,3,4)
list1.append(5)
print(list1)
#tuple1.append(5)
#this will give error as tuple is immutable

print(tuple1)
print(tuple1[1])
print(tuple1[-1])

#concatenation
tuple2="a","b","c","d","e"
print(tuple2)
print(tuple1)
tup=tuple1+tuple2
print(tup)

#nesting
nest=(tuple1,tuple2)
print(nest)

#accessing elements of nested tuples
print(nest[0][-1])

#repetion
rep=("python",)*5
print(rep)
rep2=("python",)
print(rep2*10)
print(rep2)

#slicing
slice_tuple=tuple1[:3]
print(slice_tuple)
#checking if an element exists in a tuple
if "3" not in slice_tuple:
    print("element does not exist")
else:
    print("element exists")
