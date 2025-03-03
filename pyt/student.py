print("Qustion---> Create a dictionary with the roll number, name and marks of n students in a class and display the names of students who have marks above 75.")
dictionary=dict()
i=1
f=0
n=int(input("Enter number of enteries:"))
while i<=n:
    name=input("Enter name of students:")
    rn=input("Enter roll number of student:")
    cs=input("Enter class and section of student:")
    m=input("Marks obtained by student:")
    a=(name,cs,m)
    dictionary[rn]=a
    i=i+1
b=dictionary.keys()
for c in b:
    c=dictionary[b]
    if eval(c[2])>75:
            print(c[0],"Roll Number:",b,"has scored",c[2])
