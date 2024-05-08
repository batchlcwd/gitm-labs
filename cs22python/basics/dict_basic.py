user ={
    'username':'lcwd405',
    'email':'lcwd@gmail.com',
    'password':'12345'
}

#access
print(user['email'])

#modify
user['email']='newlcwd@GMAIL.COM'

print(user['email'])

# methods to perform operatons on dict
un=user.get('username')
print(un)

keys=user.keys()
for k in keys:
    print(k," = >",user.get(k))

