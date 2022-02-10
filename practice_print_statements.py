# single commenting is done by using (#)

"""Multiple line commenting
is done in this method"""

# Introduction to print statement
print("Introduction to python")
print(7)

# Introduction to variables(constant)
a = 1         # assigned 1(integer) to variable a
print(a)
print("Value of a is ", a)       # printing variable a
print(type(a))
b = "Hello world"       # assigned Hello world(string) to variable b
print("value of b: ", b)                # printing variable b
print("Type of b is ",type(b))

# Another type of printing
c = 1

d = "Hello world"

print("value of c is {} and value of d: {}".format(c, d))

print("type of c is {} and type of d: {}".format(type(c), type(d)))

val = "1"

print("value of c is {}, value of d is {} and value of val is {}".format(c, d, val))

# Changing of existing values of variables

a = 2
print("changed value of a:", a)

x = 5
y = 8
z = x+y
print("Sum of x and y is", z)

a = 45
b = 8
c = a**2 + b**2
print("square of c", c**2)

a = 16
b = 81
c = 49
d = 25
x = a+b+c+d
y = a*b*c*d
z = a+b*c-d
print(" value of x is {},and value of y is {},and value of z is{}".format(x,y,z))

a = 99898
b = 45678
c = 2344
d = 9876
x = a*c*d-b
y = a/b*c-d
z = a-d+c*b
print(" value of x is {},and value of y is {},and value of z is{}".format(x,y,z))

n = 81
d = 49
p = 256
x = n*d*p-p*d/n+d+p*d
y = p*d*n*d*p-p*d/n+d+p*d
z = n*d*p-p*d/n+d+p*d*n*d*p-p*d/n+d+p*d
print(" value of x is {},and value of y is {},and value of z is {}".format(x,y,z))

# what is string ?
# String is a colection of alphabets, words or numbers or combination of any which are declared inside double quotes or a single quote
#example


str1 = "python"               #collection of alphabets
str2 = "1234"                 #collection of numbers
str3 = "python123"            #collection of combination of numbers and alphabets(alphanumerics)
str4 = 'python@123'           #collection of alphanumeric and symbols

# concatination of string
conc_str1_and_str2 = str1 + str2
print("concatination of str1 and str2 is {}".format(conc_str1_and_str2))





