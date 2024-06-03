#3. function with defaut parameters

#4. function with different parameter order
def get_fullname(first='FirstName',last='LastName'):
    print(first+" "+last)

#5. function with variable arguments(var args)
def print_numbers(*vars):
    print(vars)
    print(type(vars))
    sum=0
    for i in vars:
        sum=sum+i 
    print("sum is ",sum)


    


get_fullname("john",'sharma')
get_fullname()
get_fullname("ashutosh")
get_fullname(last='sharma',first='virat')

print_numbers(3,4,5,6,7,8)
print_numbers(3,4)





