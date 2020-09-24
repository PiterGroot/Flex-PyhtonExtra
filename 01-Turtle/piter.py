import turtle
colors = [ "red","purple","blue","green","orange","yellow"]
venster = turtle.getscreen()
turtle.speed(0)
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(100):
   venster.bgcolor(colors[x % 6])
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   turtle.circle(x)
   my_pen.left(10)

turtle.goto(0, -20)

for x in range(70):
   venster.bgcolor(colors[x % 6])
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   turtle.circle(x)
   my_pen.left(10)

turtle.goto(0, -40)

for x in range(50):
   venster.bgcolor(colors[x % 6])
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   turtle.circle(x)
   my_pen.left(10)

turtle.goto(0, -60)

for x in range(-60):
   venster.bgcolor(colors[x % 6])
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   turtle.circle(x)
   my_pen.left(10)

turtle.done()
