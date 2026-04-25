import turtle


screen = turtle.Turtle()
screen.speed(10)

for i in range(4):
    screen.color("red")
    screen.forward(100)
    screen.right(90)
    

for i in range(4):
    screen.color("blue")
    screen.forward(100)
    screen.left(90)
    
screen.right(180)

for i in range(2):
    screen.color("pink")
    screen.forward(180)
    screen.left(90)
    screen.forward(20)
    screen.left(90)
    
screen.color("green")
screen.circle(60)
   
turtle.done()