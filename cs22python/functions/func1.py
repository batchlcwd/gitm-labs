#going to create function

def test123_():
    print("I am function...")
    print("working for you...")


# formal parameters
def sum(a,b):
    print("going to add two values")
    s=a+b 
    print("sum is ",s)

def length(str):
    # count number of characters
    count=0
    for ch in str:
        count= count+1
    print("count[function]: ",count)
    return count

# input()
# int() 
# float() 
# type() 


test123_()
test123_()
test123_()
test123_()

# actual parameters
sum(12,23)
sum(11,101)
length("abc")
count_value=length("python is amazing")
print("Received Count[own] ",count_value)
