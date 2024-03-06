#various ways to read data from a file
f=open('myfile.txt', 'w')
L=['This is Paris \nThis is Nairobi\nThis is Cairo']

f.write('Hello!\n')
f.writelines(L)
f.close()

#changing access modes
f=open('myfile.txt','r+')
print('Output of Read function is: ')
print(f.read())
print()

f.seek(0)

print('Output of Readline() function is:')
print(f.readline())
print()

f.seek(0)

print('Output of Read(9) function is:')
print(f.read(9))
print()

f.seek(0)

print('Output of Readlines function is:')
print(f.readlines())
f.close()