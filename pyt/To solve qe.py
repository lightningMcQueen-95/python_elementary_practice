import cmath
a = int(input("Please enter leading cofficiect:"))
b =int(input("Please enter cofficiect of x:"))
c = int(input("Please enter constant term:"))
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print("The solution are:",sol1,sol2)


