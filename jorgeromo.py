import turtle

def draw_bowl():
    turtle.penup()
    turtle.goto(0, -150)
    turtle.pendown()
    turtle.color('#ffb6c1')  # Pink color
    turtle.begin_fill()
    turtle.circle(150, 180)
    turtle.goto(-150, -150)
    turtle.goto(150, -150)
    turtle.goto(0, -150)
    turtle.end_fill()

def draw_noodles():
    turtle.penup()
    turtle.goto(-100, -50)
    turtle.pendown()
    turtle.color('gold')
    for i in range(5):
        turtle.setheading(60 + i * 10)
        turtle.circle(100, 60)
        turtle.penup()
        turtle.goto(-100 + i * 40, -50)
        turtle.pendown()

def draw_pork_chop(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('#deb887')
    turtle.begin_fill()
    turtle.circle(35)
    turtle.end_fill()
    turtle.color('#a0522d')
    turtle.width(3)
    turtle.circle(35, 180)
    turtle.width(1)

def draw_egg(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('white')
    turtle.begin_fill()
    turtle.setheading(45)
    for _ in range(2):
        turtle.circle(30,90)
        turtle.circle(30//2,90)
    turtle.end_fill()
    # Yolk
    turtle.penup()
    turtle.goto(x+10, y+10)
    turtle.pendown()
    turtle.color('#ffe066')
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()

def draw_naruto(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color('white')
    turtle.begin_fill()
    for _ in range(18):
        turtle.forward(20)
        turtle.left(100)
    turtle.end_fill()
    # Pink swirl
    turtle.penup()
    turtle.goto(x+5, y+5)
    turtle.pendown()
    turtle.color('pink')
    turtle.width(2)
    turtle.setheading(0)
    for i in range(18):
        turtle.forward(1.5)
        turtle.left(20)
    turtle.width(1)

def draw_green_onions():
    positions = [(-30, 10), (0, 30), (40, 0), (60, 20)]
    for x, y in positions:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color('green')
        turtle.width(5)
        turtle.setheading(90)
        turtle.forward(20)
        turtle.width(1)

def draw_seaweed():
    positions = [(-80, 60), (-60, 80), (-40, 70)]
    for x, y in positions:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.color('#2e8b57')
        turtle.begin_fill()
        for _ in range(2):
            turtle.forward(10)
            turtle.left(120)
            turtle.forward(30)
            turtle.left(60)
        turtle.end_fill()

def main():
    turtle.speed(0)
    turtle.bgcolor('white')
    draw_bowl()
    draw_noodles()
    draw_pork_chop(-40, 0)
    draw_pork_chop(40, 20)
    draw_egg(60, -30)
    draw_naruto(0, 40)
    draw_green_onions()
    draw_seaweed()
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
