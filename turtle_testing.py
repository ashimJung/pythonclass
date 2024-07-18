
import turtle

 
turtle.bgcolor('black')
t=turtle.Turtle()
t.speed(0)

colors=['red','dark red']

for number in range(200):
   t.forward(number-3)
   t.right(33.33)
   t.pencolor(colors[number%2]) # type: ignore
turtle.done()
 # type: ignore