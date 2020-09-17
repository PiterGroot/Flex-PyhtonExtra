import turtle
colors = [ "red","purple","blue","green","orange","yellow"]
venster = turtle.getscreen()
turtle.speed(0)
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   venster.bgcolor(colors[x % 6])
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   turtle.circle(x)
   my_pen.left(30)


turtle.done()
