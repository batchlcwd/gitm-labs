#open the file
filename=input("Enter file name: ")
file_ref=open(filename,'w')

#write operation

content=input("Enter file content: ")

file_ref.write(content)

print("written successfully...")
#close the file
file_ref.close()
