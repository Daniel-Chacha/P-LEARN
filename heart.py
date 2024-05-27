def triangle(size):
    for i in range(0, size , 2 ):
        yield ' ' *(i//2) +'*' * (size -i) + ' ' *(i//2)

 
def heartpattern():
    for j in reversed(list(triangle(4))):
        print(j,j)
    for j in triangle(9):
        print(j)
    

heartpattern()
