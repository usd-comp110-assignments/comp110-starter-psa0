import turtle


# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)

# Draw bowl
t.penup()
t.goto(0, -100)
t.pendown()
t.color("saddlebrown")
t.begin_fill()
t.circle(120)
t.end_fill()

# Draw broth
t.penup()
t.goto(0, -80)
t.pendown()
t.color("goldenrod")
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw noodles
t.color("khaki")
for i in range(10):
    t.penup()
    t.goto(-60 + i*12, 0)
    t.pendown()
    t.setheading(-90)
    t.circle(40, 180)

# Draw toppings (egg)
t.penup()
t.goto(-40, 40)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(-40, 55)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(8)
t.end_fill()

# Draw toppings (green onions)
t.penup()
t.goto(30, 60)
t.pendown()
t.color("green")
t.begin_fill()
t.circle(7)
t.end_fill()

t.penup()
t.goto(50, 40)
t.pendown()
t.begin_fill()
t.circle(5)
t.end_fill()

# Hide turtle and finish
t.hideturtle()
turtle.done()
