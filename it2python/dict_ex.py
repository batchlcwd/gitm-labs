#creting dict of raman

details={
    "name":"raman",
    "phone":'23423515',
    'roll_number':2002,
    'college':'gitm',
    'department':'it',
    'subjects':['oops','python','java'],
    'friends':[
        {
            'name':'John',
            'phone':'987654',
            'college':'iit'
        },
        {
            'name':'David',
            'phone':'235235',
            'college':'hbti'
        }
    ]

    
}
print(details)
print(details['name'])
print(details['department'])
print(details['college'])
print(details['subjects'][::-1])
print(len(details['subjects']))
print(details['friends'])

print(details['friends'][0]['name'])