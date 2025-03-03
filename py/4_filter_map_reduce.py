#def is_even(x):
 #   return True if x % 2 == 0 else False
from functools import reduce
num=[3,2,4,8,7,9]
evens=list(filter(lambda n:n%2==0,num))

doubles=list(map(lambda n:n+2,evens))

sum=reduce(lambda a,b:a+b,doubles)

print(evens)
print(doubles)
print(sum)

