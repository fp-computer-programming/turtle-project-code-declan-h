#author DMH 

import turtle

window = turtle.Screen() # window for the turtle
window.setup(1000, 1000)
window.screensize(100,100)

Declan = turtle.Turtle()





def move_forward():
    if Declan.direction != "Up":
        Declan
    elif Declan.direction == "Down":
        Declan.direction == "Up"
        Declan.forward(50)




window.onkey(move_forward, "Up")

def move_right():
    Declan.right(90)
    Declan.forward(50)

window.onkey(move_right, "Right")

def move_left():
    Declan.left(90)
    Declan.forward(50)

window.onkey(move_left, "Left")

def move_down():
    Declan.right(180)
    Declan.forward(50)






window.listen()


window.mainloop()

