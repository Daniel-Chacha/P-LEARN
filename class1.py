class dog:
    animal='dog'

    def __init__(self,breed,color):
        self.breed=breed
        self.color=color

rodger=dog('Pug','brown')
buzo=dog('Bulldog','red')

print("Rodger's details")
print('Rodger is a'+rodger.animal)
print('Breed:', rodger.breed)
print('Color:',rodger.color)


print('\n\nBuzo details')
print('Buzo is ',buzo.animal)
print('Breed:',buzo.breed)
print('Color:' ,buzo.color)

print('\n\nAccessing the class variable')
print(dog.animal)