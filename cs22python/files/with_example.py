

# if you want handle exceptions:

try:
    with open('db.pyasfaf','r') as file_ref:
        print(file_ref.read())

except:
    print("hello, how are you, your filename is invalid !! try again with different one..")