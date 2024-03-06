#reading data from a file

f=open('greek.txt','r')
for x in f:
    print(x)

f.close()
