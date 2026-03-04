import turtle
t = turtle.Turtle()
t.speed(0)  
def rect(color, x, y, w, h):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for side in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    t.end_fill()

rect("black", -200, 100, 400, 80)

rect("white", -200, 20, 400, 80)

rect("green", -200, -60, 400, 80)

t.penup()
t.goto(-200, 100)   
t.pendown()
t.color("red")
t.begin_fill()
t.goto(-200, -140)     
t.goto(-80, -15)       
t.goto(-200, 100)    
t.end_fill()

t.hideturtle()

turtle.done()
