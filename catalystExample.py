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
    t.pensize(3)
    t.penup()
    t.goto(0, 10)
    t.pendown()
    t.setheading(0)
    # Draw a large spiral for spaghetti
    for i in range(300):
        t.forward(1.2 + i * 0.04)
        t.left(5)
    # Add a second spiral for fullness
    t.penup()
    t.goto(-10, 0)
    t.pendown()
    t.setheading(10)
    for i in range(250):
        t.forward(1.1 + i * 0.035)
        t.left(5)
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
    # Draw red sauce under spaghetti
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.color("#c0392b")
    t.begin_fill()
    t.setheading(0)
    for i in range(180):
        t.forward(1.5 + i * 0.08)
        t.left(2)
    t.end_fill()
    draw_spaghetti()

    # Meatballs (spread out)
    draw_meatball(-70, 40)
    draw_meatball(60, 20)
    draw_meatball(-10, 70)
    
    # Basil leaves
    draw_basil(-20, 60)
    draw_basil(20, 35)
    draw_basil(10, 0)
    t.hideturtle()

# Draw the scene
draw_all()
turtle.done()
