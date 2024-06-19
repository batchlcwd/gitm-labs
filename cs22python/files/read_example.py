#open the file

#open(file,mode) 
#full path
filename=input("Enter file name:")
file_ref=open(filename,'r')

#operations

content=file_ref.read()

print(content)

#file close
file_ref.close()