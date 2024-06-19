#open
file_ref=open(input("Enter filename: "),'w')



#operation
content=input("Enter content: ")
file_ref.write(content)
print("written successfully..")
#close

file_ref.close()