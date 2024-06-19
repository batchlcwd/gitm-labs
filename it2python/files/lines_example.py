#program to read the content from file

#1. open the file
#open(filename,mode)
filename=input("Enter file name:")
file_ref=open(filename,'r')


#2. read the content

lines_list=file_ref.readlines()
print("number of lines: ",len(lines_list))
# print(lines_list)
for line in lines_list:
    print(line,end='')

#3. file ko close

file_ref.close()