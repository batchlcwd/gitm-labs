# function to count digits

def count_digits(n):
    count=0
    # n=1241
    while n>0:
        #last digit nikal rha hai
        last_digit=n%10
        #count ko track kar rha hai
        count=count+1
        # number se last digit hata rha hai
        n=n//10
    return count


#calling function
n=int(input("Enter number : "))
digits=count_digits(n)
print(digits)