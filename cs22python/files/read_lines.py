#open the file

#open(file,mode) 
#full path
filename=input("Enter file name:")
file_ref=open(filename,'r')

#operations
#data line by line
content=file_ref.readlines()
print("Number of line in file : ",len(content))
# print(content)
for line in content:
    print(line,end='')
    words=line.split(' ')
    print("\t",'Words : ',len(words))

#file close
file_ref.close()