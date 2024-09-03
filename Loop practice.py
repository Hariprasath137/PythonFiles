
#get the input and find the cube value

"""num = int(input())

for i in range (1,num+1):
    j=(i*i*i)
    print("the number is ",i, "and the cube of the ",i,"is",j)"""


    
#print 2 table using for loop
"""sum = 0
for i in range(1,11):
    sum = sum+2
    print(i,"x 2 =",sum)"""


"""for i in range(1,11):
    print(i,"x 2 =",i*2)"""


#get input of two number and print inbetween the numbers 
         
"""num1 = int(input("Enter the number 1:"))
num2 = int(input("Enter the number 2:"))

for i in range  (num1+1,num2):
    print(i) """

#Get input and print inbetween even number only

"""
num1 = int(input())
num2 = int(input())

for i in range(num1,num2):
    if(i%2==0):
        print(i)
        """

#Get input and Count the number of odd and even

"""a = int(input())
b = int(input())

count = 0

for i in range(a,b):
    if(i%2==0):
        count = count+1
print("the even number count is ",count)
if(i%2!=0):
        count = count+1
print("The odd number count is ",count)"""



#get input two numbers and Count the number which are divisible by 3 and 5

"""a = int(input())
b = int(input())

count = 0

for i in range(a,b):
    if(i%3==0 and i%5==0):
        count = count+1
print (count)"""

#write the program to find the sum of the numbers

"""a = int(input())
b = int(input())

sum = 0

for i in range(a,b+1):
    sum = sum+i
print(sum)
"""

#write a program to read any 10 numbers from the keyboard and find the sum and average
"""a =[1,2,3,4,5,6,7,8,9,10]
sum = 0

for i in a:
    a = int(input("Enter any number:"))
    sum = sum+a
print("The number of the sum is ",sum)

ave = sum/10

print("The total average is ",ave)
"""

#another method using append 

a = []
sum = 0


for i in range(1,11):
    num = int(input())
    sum = sum+i
    a.append(num)
print(a)
print (sum)
Ave = sum/i
print(Ave)








































