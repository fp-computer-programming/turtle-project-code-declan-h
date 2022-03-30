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
    Declan.forward(50)

def move_right():
    Declan.setheading(0)
    Declan.forward(50)

def move_left():
    Declan.setheading(180)
    Declan.forward(50)

def move_down():
    Declan.setheading(270)
    Declan.forward(50)
    

#moving key binds 
window.onkey(move_left,"Left")

window.onkey(move_right,"Right")

window.onkey(move_up,"Up")

window.onkey(move_down,"Down")

window.listen()

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle()




#making boundary untouchable    
while True:
    #boundary x cord
    if Declan.xcor() > 290 or Declan.xcor() < -290:
        Declan.right(180)

    #boundary y cord 
    if Declan.ycor() > 290 or Declan.ycor() < -290:
        Declan.right(180)






window.mainloop()

