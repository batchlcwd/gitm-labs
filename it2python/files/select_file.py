#manual filename
#full manully

from tkinter import filedialog , messagebox

file=filedialog.askopenfile(title='Select file to open')
print(file.name)
with open(file.name,'r') as ref:
    cont=ref.read()
    messagebox.showinfo(title="file content",message=cont)
  