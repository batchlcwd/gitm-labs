#open
file_ref=open('write.txt','w')



#operation
content='this is content \n that we are going to write in file using python program'
file_ref.write(content)
print("written successfully..")
#close

file_ref.close()