#program to read the content from file

#1. open the file
#open(filename,mode)
filename=input("Enter file name:")
file_ref=open(filename,'r')


#2. read the content

cont=file_ref.read()


print(cont)

#3. file ko close

file_ref.close()