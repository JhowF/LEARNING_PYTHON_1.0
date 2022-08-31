from turtle import *
bgcolor('black')
speed(0)
hideturtle()
for i in range (120) :
    color('red')
    circle(i)
    color('orange')
    circle(i*0.8)
    right(3)
    forward(3)
done()

#from turtle import *
#bgcolor('blue')
#speed(-5)
#getturtle()
#for i in range (150) :
#    color('white')
#    circle(i)
#    color('black')
#    circle(i*0.9)
#    right(2)
#    left(3)
#    forward(0)
#done()