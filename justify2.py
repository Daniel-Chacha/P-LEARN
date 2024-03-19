
picnic={
    'Cups':4,
    'Plates':5,
    'Knives':3,
    'Apples':12,
    'Sandwiches':1000
}

def pic(picdict,lw,rw):
    print('PICNIC ITEMS'.center(lw+rw,'='))
    for x,y in picdict.items():
        print(x.ljust(lw,'.'),str(y).rjust(rw))


a=pic(picnic,20,5)
print(a)

