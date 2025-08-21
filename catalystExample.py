import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)

def draw_plate():
    t.penup()
    t.goto(0, -120)
    t.pendown()
    t.color("lightgray")
    t.begin_fill()
    t.circle(150)
    t.end_fill()
    # Plate rim
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.color("gray")
    t.width(3)
    t.circle(120)
    t.width(1)

def draw_spaghetti():
    t.color("#f5e6b2")  # pasta color
    for i in range(18):
        t.penup()
        t.goto(-60 + (i % 6) * 24, -20 + (i // 6) * 20)
        t.pendown()
        t.setheading(60 + (i % 3) * 30)
        t.pensize(3)
        t.circle(40, 120)
    t.pensize(1)

def draw_meatball(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#8b4513")
    t.begin_fill()
    t.circle(22)
    t.end_fill()
    # Meatball highlight
    t.penup()
    t.goto(x + 10, y + 15)
    t.pendown()
    t.color("#a0522d")
    t.begin_fill()
    t.circle(7)
    t.end_fill()

def draw_basil(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#228B22")
    t.setheading(45)
    t.begin_fill()
    for _ in range(2):
        t.circle(10, 90)
        t.left(90)
    t.end_fill()
    t.setheading(135)
    t.begin_fill()
    for _ in range(2):
        t.circle(10, 90)
        t.left(90)
    t.end_fill()

def draw_all():
    draw_plate()
    draw_spaghetti()
    # Meatballs
    draw_meatball(-40, 20)
    draw_meatball(30, 10)
    draw_meatball(0, 50)
    # Basil leaves
    draw_basil(-20, 60)
    draw_basil(20, 35)
    draw_basil(10, 0)
    t.hideturtle()

# Draw the scene
draw_all()
turtle.done()
