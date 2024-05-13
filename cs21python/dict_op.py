# key-value pair

developer={
    "name":"Rahul",
    "position":"Web Developer",
    "age":25,
    "salary":250000,
    'is_active':True
}

print(developer)

# list[0]
print(developer['name'])
print(developer['age'])
print(developer['position'])

# list[0]=89

developer['age']=36
developer['name']="Arvind"
print(developer)

# key access
# value modify

name=developer.get('Name',"John")
print(name)

n=developer.pop("firstname","Default Name")
print(n)
print(developer)

keys=developer.keys()
print(keys)

for k in keys:
    print(k, developer.get(k))

values=developer.values()
print(values)   
for v in values:
    print(v)





