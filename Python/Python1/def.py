def sumation(w,e):
    c=w+e
    return c
def sub(p,q):
    o=p-q
    return o
def mul(d,f):
    t=d*f
    return t
#main
a=int(input("Enter first number"))
b=int(input("Enter second number"))
r=sumation(a,b)
s=sub(a,b)
t=mul(r,s)
print("sum is %s, substaction is %s and multiplicaiton is %s"%( r,s,t))
