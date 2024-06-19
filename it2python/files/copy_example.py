file_from_name=input("Enter file 1: ")
file_to_name=input('Enter file 2:')
with open(file_from_name,'r') as file_from_ref:
    content=file_from_ref.read()
    with open(file_to_name,'w') as file_to_ref:
        file_to_ref.write(content)
        print("file copied")
