#open the file
filename=input("Enter file name: ")
file_ref=open(filename,'w')

#write operation
lines=[]
print("Enter content line by line [Press any time \' quite \'] to exit:")
while True:
    line=input()
    if line=='quite':
        break
    else:
        lines.append(line+'\n')

file_ref.writelines(lines)


print("written successfully...")
#close the file
file_ref.close()
