#author DMH 

import turtle


#setting up window
window = turtle.Screen() 
window.setup(1000, 1000)
window.screensize(100,100)
Declan = turtle.Turtle()






#moving functions 
def move_up():
    Declan.setheading(90)
    Declan.forward(20)

def move_right():
    Declan.setheading(0)
    Declan.forward(20)

def move_left():
    Declan.setheading(180)
    Declan.forward(20)

def move_down():
    Declan.setheading(270)
    Declan.forward(20)
    

#moving key binds 
window.onkey(move_left,"Left")

window.onkey(move_right,"Right")

window.onkey(move_up,"Up")

window.onkey(move_down,"Down")

window.listen()

# Draw border of maze
mypen = turtle.Turtle()
maze1 = turtle.Turtle()
mypen.hideturtle()
mypen.speed(10)
mypen.penup()
mypen.setposition(-400,-300)
mypen.pendown()
mypen.pensize(2)
mypen.forward(700)
mypen.penup()
mypen.forward(50)
mypen.pendown()
mypen.left(90)
mypen.forward(650)
mypen.left(90)
mypen.forward(700)
mypen.penup()
mypen.forward(50)
mypen.pendown()
mypen.left(90)
mypen.forward(650)
mypen.hideturtle()



maze1.speed(0)
maze1.penup()
maze1.setposition(300,-300)
maze1.pendown()
maze1.left(90)
maze1.forward(50)
maze1.left(90)
maze1.forward(100)
maze1.right(90)
maze1.forward(100)
maze1.penup()
maze1.forward(50)
maze1.pendown()
maze1.left(90)
maze1.forward(150)
maze1.left(90)
maze1.forward(150)
maze1.left(90)
maze1.forward(50)
maze1.right(90)
maze1.forward(50)
maze1.right(180)
maze1.forward(150)
maze1.right(90)
maze1.forward(50)
maze1.right(90)
maze1.forward(100)
maze1.penup()
maze1.left(90)
maze1.forward(100)
maze1.pendown()
maze1.left(90)
maze1.forward(100)
maze1.penup()
maze1.forward(50)
maze1.pendown()
maze1.forward(50)
maze1.left(90)
maze1.forward(250)
maze1.left(90)
maze1.forward(150)
maze1.penup()
maze1.forward(50)
maze1.pendown()
maze1.left(90)
maze1.forward(50)

#making boundary untouchable    

    #boundary x cord
if Declan.xcor() > 290 or Declan.xcor() < -290:
    Declan.right(180)

    #boundary y cord 
if Declan.ycor() > 290 or Declan.ycor() < -290:
    Declan.right(180)






Declan.penup()
Declan.setposition(330,-320)
Declan.pendown()



window.mainloop()

