with open('file2.txt','w') as f:
    data = ['This is the first line', 'This is the second line', 'This is the third line']

    for line in data:
        f.write(line +'\n')

        print(line)