name='substring'
#indexing
print(name[1])

#slicing
print(name[1:5])

#other
#python ne hame bahut sare string ke feature/methods  de rakhe hai.
# name='substring'
index=name.index('b')
print(index)

result=name.startswith('ubb')

print(result)
print(name.endswith("ing"))
number="12415"
print(number.isdigit())

id="_abc_abc_56()"
print(id.isidentifier())
print(name.lower())
print(name.upper())

s1="subsutringsu"
s2="technologies"
s3="**"
print(s3.join([s1,s2,"ok","its nice"]))

new_str=s1.replace('su','ab',2)
print(new_str)

#split

channel_name="Learn Code With Durgesh"
name_list=channel_name.split(' ')
print(name_list)

for name in name_list:
    print(name.upper(),len(name))


