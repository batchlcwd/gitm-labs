# variable argument function
def pintu(*vars):
    print(vars)
    print(type(vars))
    sum=0
    for i in vars:
        sum=sum+i
    print("sum ",sum)

pintu(1,2,3,6)
pintu(1,2)
pintu(2,3,53,23,53,23,53,64,64,34,646,'str')

