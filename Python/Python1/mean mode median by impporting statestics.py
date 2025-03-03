import statistics
l1=[ ]
n=int(input("Enter the no. of elements"))
i=0
while i<n:
    k=int(input("Enter the element"))
    l1.append(k)
    i+=1
m1=statistics.mean(l1)
m2=statistics.mode(l1)
m3=statistics.median(l1)
print("The mean is %s, median is %s and mode is %s"%(m1,m3,m2))
