

#WAP to print factorial of each digit of number

# 33534

# 4 -> 4*3*2*1=?
# 3 -> 3*2*1= ?
# 5 -> 5*4*3*2*1=?

def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i 
    return f 

#take number
number=int(input("Enter number: "))
n2=number
while number>0:
    digit=number %10 
    print(digit,"=>",factorial(digit))
    number=number//10
import math
sq=math.sqrt(n2)
print(sq)

# math.pow(10,78)
