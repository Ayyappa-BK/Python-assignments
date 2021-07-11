str1 = 'hello world'
str2 = "WELCOME TO BANGALORE"

#capitalize the first character to upper case
x = str1.capitalize()
print(x)

#returns the centered string
x1 = str1.center(20)
print(x1)

#returns the number of times a specified value occurs in a string
x2 = str1.count('l')
print(x2)

#returns true if the string ends with the specified value
x3 = str1.endswith('d')
print(x3)

#searching the string for a specified value and returns the position of where it was found
x4 = str1.index('w')
print(x4)

#converts a string into lower case
x5 = str2.lower()
print(x5)

#returns a tuple where the string is parted into three  parts
x6 = str2.partition('TO')
print(x6)

#splits the string at the specified separator and returns a list
x7 = str2.split()
print(x7)

#converts a string into upper case
x8 = str1.upper()
print(x8)