friends=[]
x=30
# l1={
#         "brand":'Apple',
#         'name':'macbook air',
#         'price':24000,
#         'processor':'Intel i7'
#     }
# creating dict
rams_detail= {
    'name':'Ram',   
    'college':'Gitm lko',
    'friends':['Shyam','Ajay'],
    'laptops':[{
        "brand":'Apple',
        'name':'macbook air',
        'price':24000,
        'processor':'Intel i7'
    },{
        'brand':'Apple',
        'name':'macbook PRO',
        'price':240000,
        'processor':'Apple m2'
    },
    {
        'brand':'HP',
        'name':'HP32525',
        'price':240,
        'processor':'Intel i7'
    }]


#dict --> list --> collection of dict

}

# using dict

print(rams_detail['name'])
print(rams_detail['friends'])
print(len(rams_detail['friends']))
print(len(rams_detail['laptops']))
print(rams_detail['laptops'])
print(rams_detail['laptops'][0]['brand'])
print(rams_detail['laptops'][1]['name'])


