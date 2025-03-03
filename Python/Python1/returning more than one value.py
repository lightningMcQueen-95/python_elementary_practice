def calc(l,b):
    area=l*b
    peri=2*(l+b)
    return area,peri
#main
a=int(input("enter the length:"))
b=int(input("enter the breath:"))
x,y=calc(a,b)
print("Area is ",x)
print("perinmeter is ",y)
