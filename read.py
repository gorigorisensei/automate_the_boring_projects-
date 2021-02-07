import os

a = os.getcwd()
print(a)
fufile=open('fufufui.rtf', 'w+')
fufile.write('unko!!!!!!!!!!')

content = fufile.read() 
print(content)
