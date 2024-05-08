# dict operations
#add
#delete
#update
#get value by key

person={
    "name":"John",
    "phone":352525,
    "isActive":True
}

# name value
print(person["name"])
print(person["phone"])

#update 

person["name"]="Sita Ram"
print(person)

# print all values
# python ne bahut sare methods/functions de diya hai operations perform karne ke lie

# person={
#     "name":"John",
#     "phone":352525,
#     "isActive":True
# }

value=person.get("name")
print(value)

#get(key,default)
value1=person.get("phoneNumber","12345")
print(value1)

removed_value=person.pop("phoneNumber","default value")
print(removed_value)
print(person)


# person.clear()

# key ==> value

# sari keys nikalini hai

keys=person.keys()
print(keys)

for k in keys:
    print(k,person.get(k))
    print("hi")

if True:
    print("inside if")
    print("ok")
    print("how are you?")
else:
    print("insde else block")
    print("what's up?")
    if False:
        print("insde else... if")
    pritn("inside else block")


   
#sari values nikali hai

values=person.values()
for value in values:
    print(value)

if True:
    print("key is there and its value is")
else:
    pass 