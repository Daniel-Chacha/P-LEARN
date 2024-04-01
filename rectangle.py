# drawing a rectangle

def rectangle(symbol,length,width):
    print(symbol*length)
    for i in range(width-2):
        print(symbol + (' '*(length-2))+symbol)
    print(symbol*length)


rectangle('x',20,10)