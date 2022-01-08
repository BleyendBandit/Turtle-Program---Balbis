import turtle

x = int(input("Enter the dimension: "))

Length = x * 5
Width = x
insideLength = Length / 2.5
Angle = 90


turtle.setup(200, 200)
turtle.showturtle()
turtle.speed(0)
turtle.penup()
turtle.pencolor("blue")
turtle.pensize(5)
turtle.turtlesize(2)
turtle.goto(0, 0)
turtle.pendown()

for count in range(2):
    turtle.forward(Length)
    turtle.right(Angle)
    turtle.pencolor("red")
    turtle.forward(insideLength)
    turtle.left(Angle)
    turtle.pencolor("cyan")
    turtle.forward(Width)
    turtle.pencolor("magenta")
    turtle.left(Angle)
    turtle.forward(Length) 
    turtle.pencolor("yellow")
    turtle.left(Angle)
    turtle.forward(Width)
    turtle.left(Angle)
    turtle.pencolor("purple")
    turtle.forward(insideLength)
    turtle.right(Angle)
    turtle.pencolor("pink")

exit = input('')
