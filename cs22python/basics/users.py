user={
    'username':'John304',
    'name':'John Peter',
    'email':'lcwd@gmail.com',
    'password':'abc123',
    'dob':'01-01-9001',
    'mobileno':'+91-989889898',
    'is_active':False ,
    'followers':[{
        'name':'ramu',
        'email':'ramu@gmail.com'
    },
    {
        'name':'shyamu',
        'email':'shyam@gmail.com'
    },
     {
        'name':'shyamu',
        'email':'shyam1@gmail.com'
    },{
        'name':'rampal',
        'email':'rampal@gmail.com'
    }],
    'follwings':[{
        'name':'john',
        'email':'john@gmail.com'
    },
  ]

}


#1. user-> name,email,mobileno
print("Name : ",user['name'])
print('Mobile Number : ', user['mobileno'])
print('Password: ', user['password'])

#2. number of followers
followers=user['followers']
#3. print(followers)
print("number of followers : ",len(followers))

#print the emails of the followers
# single_follower=followers[0]
# second_follower=followers[1]
# print(single_follower['email'])
# print(second_follower['email'])
# 4.
print(f'followers of {user['name']}')
for follower in followers:
    print("Name : ",follower['name'])
    print("Email : ",follower['email'])
    print("-----------------------------")

print("++++++++++++++++++++++++++++++++++++")

# 5.
if user['is_active']==True:
    print(f"{user['username']} is active")
else:
    print(f"{user['username']}  is not active")

# 6.
#followers + following 

ffolowers=user['followers']+user['follwings']
print(ffolowers)
print('number of followers and following: ',len(ffolowers))


for ff in ffolowers:
    print("Name : ",ff['name'])
    print("Email : ",ff['email'])
    print("_________")




# # printing user
# print(harshit['followers'][1]['email'])

# followers=harshit['followers']
# for follower in followers:
#     if follower['name']=='shyamu':
#         print(follower)

# if harshit['is_active']==True:
#     print("Harshit is active")
# else:
#     print("harshit is not active")




# #print '{username} is active' if  is_active is True else print '{username} is not active'