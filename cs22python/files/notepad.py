#open
file_ref=open(input("Enter filename: "),'w')


line_list=[]
print("Enter content line by line [Press \' Quit \'] to exit")
while True:
    line_content=input()
    # print(line_content)
    if line_content=='QUIT':
        print("quiting program")
        break
    else:
        line_list.append(line_content+'\n')

#operation
# content=input("Enter content: ")
# print(line_list)
file_ref.writelines(line_list)
print("written successfully..")
#close

file_ref.close()