#fun with empty body
def ramsingh13_():
    pass 

#fun without parameters and return type
# create
def shyam_singh_12_():
    print("hello i am shyam singh")
    print("how are you?") 

# with parameters and without return type
def sum(a,b,c):
    print("Sum is ",a+b+c)


# with parameters and with return type
def product(var1,var2,var3,var4):
    print("going to proudct : ")
    result=var1* var2 * var3 * var4
    return result

#default parameters
# named arugment
def chintu(paisa=100,type='pep'):
    colddrik=""
    print("going to market")
    print("buying colddrink for you sir")
    print("cost of cold drink is ",paisa)
    if type=='coca':
        colddrik='cocacola'
    elif type=='pep':
        colddrik='pepsi'
    elif type=='sp':
        colddrik='Sprite'
    else:
        colddrik='water'


    print("comming to home")
    return colddrik


# call
shyam_singh_12_()
sum(12,89,11)

sum(1,2,3)

sum(22,22,22)

proudct_result=product(1,2,3,4)
print("Printing product result",proudct_result)
    
# input()
# int()
# type()
# float()

cld=chintu(40,'coca')
print("Thankyou for ",cld)

cld1=chintu(100,'pep')
print("Thankyou for ",cld1)

print(chintu(500,'water'))

print(chintu())

print(chintu(type='coca',paisa=3000))
