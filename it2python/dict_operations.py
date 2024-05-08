user= {
    'name':'lcwd405',
    'email':'lcwd@gmail.com'
}

#accessing values
print(user['name'])
#modify
user['name']='john'
print(user['name'])

#dict functions/method to perform operations
# clear , pop , keys , values ,
email_value=user.get('email')
print(email_value)

# name_value=user.pop("phone","+91979787978")
# print(name_value)
# print(user)

view_keys=user.keys()
print(view_keys)
for key in view_keys:
    print(key)
    print(user.get(key))


print("_-------------")

list_values=user.values()
for value in list_values:
    print(value)
