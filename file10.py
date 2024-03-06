#reading a file using readline()
f=open('test.txt','r')
line=f.readline()     #read the first line

while line:
    print(line)
    line=f.readline()

f.close()