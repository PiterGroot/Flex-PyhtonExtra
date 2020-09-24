import turtle 
from random import randint
bgcolor('black')
x = 1
speed(0)
while x < 200:

 r = randint(0,255)
 g = randint(0,255)
 b = randint(0,255)
 turtle.circle(x)
 colormode(255)
 pencolor(r,g,b)
 fd(50 + x)
 rt(90.991)
 x = x+1

exitonclick()
