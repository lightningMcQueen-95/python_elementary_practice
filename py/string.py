string="Hello world"
print(string[:5])
print(string[5:])
print(string[2:5])

#inbuilt
print(string.upper())
print(string.lower())

print(string.find('_'))
print(string.find('o'))

x=(string.split())
print(x)

print(string.replace("Hello","Namaste"))

print(string.rpartition(" "))

#string concatination
stg1="good"
stg2="morning"
print(stg1+" "+stg2)
y=stg1+" "+stg2
print(y)

#string formating
s1="hey"
s2="all"
s3="there"
stg="{} {} {}!".format(s1,s3,s2)
print(stg)