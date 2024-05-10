# reading fils while splitting the lines when space is encountered
with open('greek.txt') as file:
    data=file.readlines()
    print(data)
    for line in data:
        y=line.split()
        print(y)