# 1...100 sare prime 
def is_prime(n):
    prime=True
    for i in range(2,n):
        if n % i ==0 :
            prime=False
            break 
    return prime

# start
lr=int(input("Enter lower range"))
ur=int(input("Enter upper range"))

for i in range(lr,ur+1):
    if is_prime(i):
        
        print(i)