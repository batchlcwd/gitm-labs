def sum(*vars):
    print(vars)
    print(type(vars))
    sum=0
    for i in vars:
        sum=sum+i

    print(sum)


sum(1,2,4,2,5,3,5,5,6,7,4,5,3,34,56)
sum(3,5)
sum(6,7,8)

