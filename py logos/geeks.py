import turtle
tut=turtle.Screen()
tut.bgcolor='white'
pen=turtle.Turtle()
pen.speed(20)
pen.color('green')
pen.width(10)


#backward C
for x in range(180):
    pen.forward(1)
    pen.right(1)

#up
pen.right(90)
pen.forward(50)

#right
pen.right(90)
pen.forward(130)

#down
pen.right(90)
pen.forward(50)
pen.left(90)

#forward C
for x in range(180):
    pen.backward(1)
    pen.right(1)

turtle.done()

