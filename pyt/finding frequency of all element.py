lst=eval(input("Enter list:"))
length=len(lst)
uniq=[]
dupl=[]
count=i=0
while i<length:
    element=lst[i]
    count=1
    if element not in uniq and element not in dupl:
        i=+1
        for j in range(i,length):
            if element==lst[j]:
                count=+1
            else:
                print("Element",element,"Frequency:",count)
                if count==1:
                    uniq.append(element)
                else:
                    dupl.append(element)
    else:
        i=+1
print("Original List",lst)
print("Unique Elements List",uniq)
print("Duplicates elements list",dupl)
      
