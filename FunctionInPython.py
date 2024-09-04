#create a function called add() sub() mul() div()

"""def add():
    print("Addition")
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print (a+b)

def sub():
    print("Subraction")
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print (a-b)

def mul():
    print("Multiplication")
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print (a*b)

def div():
    print("Division")
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    print (a/b)
    
div()
mul()
sub()
add()
"""

#Get the interger number from the user and pass it to the function

"""
def findevenorodd(num):
    if(num%2==0):
        print("The number is even")
    else:
        print("The number is odd")

a = int(input("Enter any number to find odd or even:"))

findevenorodd(a)
"""

#Get a input for a and b and pass it to the function let the function print from a to b

"""def printrange(a,b):
    for i in range (a,b+1):
        print (i);

a = int(input("Enter a:"))
b = int(input("Enter b:"))

printrange(a,b)"""

#set username and password and get input from user and check whether they match and return true or false

"""s_username = "Yuvabe"
s_password = "1234"

uname = input("Enter username:")
password = input("Enter password:")

def validate():
    if(s_username == uname and s_password == password):
        return ("True")
    else:
        return ("False")

a = validate()

print(a)"""

#(a+b)*c get input a and b and function called add() which shoud return the sum and multipy the sum with c

a = int(input("Enter a:"))
b = int(input("Enter b:"))

def add(a,b):
    return (a+b)

d = add(a,b)

c = int(input("Enter c:"))

mul = c*d

print(mul)
