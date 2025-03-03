def count(lst):
    even=[]
    odd=[]

    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
lst=[78,789,87,45,98,54]
even,odd=count(lst)
print(even,"\n",odd)