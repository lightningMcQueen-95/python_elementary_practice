year=int(input("Enter a Year:"))

if ((year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)):
     print("It is a Leap Year")
else:
     print("It is not a Leap Year")
