import turtle

my_turtle = turtle.Turtle()  # creates turtle
my_turtle.color('purple')    # turns turtle purple
my_turtle.rt(-150)
my_turtle.circle(120,60)     # draws cat head
my_turtle.setheading(120)    # draws left cat ear
my_turtle.forward(70)
my_turtle.setheading(-120)
my_turtle.forward(70)
my_turtle.circle(150,240)    # draws cat face
my_turtle.setheading(120)    # draws right cat ear
my_turtle.forward(70)
my_turtle.setheading(-120)
my_turtle.forward(70)
my_turtle.up()               # moves turtle to mid-face
my_turtle.setheading(240)
my_turtle.forward(100)
my_turtle.down()
my_turtle.setheading(180)    # draws cat nose
my_turtle.forward(12)
my_turtle.lt(120)
my_turtle.forward(12)
my_turtle.lt(120)
my_turtle.forward(12)
my_turtle.up()
my_turtle.forward(150)
