#writing and reading
f=open('test.txt','w+')
f.write('Hello Word')
f.seek(0)              #move the file pointer to the beginning of the file
data=f.read()
print(data)
f.close()