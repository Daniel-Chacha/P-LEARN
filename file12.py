#using with
L=['This is Paris \nThis is Nairobi\nThis is Cairo']
with open('myfile1.txt','w') as f:
    f.write('Hello World!\n')
    f.writelines(L)
    f.close()


with open('myfile1.txt','r+') as f:
    print(f.read())
