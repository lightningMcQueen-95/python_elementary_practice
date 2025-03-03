a=eval(input("Enter the list:"))
for i in a:
    if i<0:
        a.remove(i)
for j in a:
    if j%2!=0:
        a.remove(j)
print(a)
