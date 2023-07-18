#Part----->(1) Getting Started
import turtle #<---Is a Module
import winsound
#Beginner Friendly Module
#Lets you make basic graphic games like pong
#Great for making games

#Maing a Window
makingWindow = turtle.Screen()
makingWindow.title("Pong by @Abdul Hanan") #<--The title on top
makingWindow.bgcolor("black")#<--The background Colour
makingWindow.setup(width=800,height=600)#<--The Display Size
makingWindow.tracer(0) #<--Stops the Window from updating, We have to manually update it,(Basically Speed up our games)

#PADDLE A
paddle_a = turtle.Turtle() #It's a Turtle object
paddle_a.speed(0)#This is not the speed at which the paddle moves at the screen, it's the speed of animation and will set the speed to maximum possible speed without slowing down 
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()#<-- Turtle by definition draw a line, even thou we don't need one, And this program doesn't does does this
paddle_a.goto(-350, 0)#<-- Always remember that that (0,0) codinnates are in the middle 

#PADDLE B
paddle_b = turtle.Turtle() 
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#BALL
ball = turtle.Turtle() #<Small t for the Module name and the large T for the Class name
ball.speed(1)
ball.shape("circle")
ball.color("Red")
ball.penup()
ball.goto(0, 0)

#Score
score_a = 0
score_b = 0

#Pen( For Score)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0" ,align="center",font=("Courier", 24 ,"normal" ))

ball.dx= 0.2 #<-- Ball speed(Basically what it will do is it will move the ball)
ball.dy= -0.2 #SAME FOR BOTH (delta-d(x and y))
#Functions to move
def paddle_a_up():
    y = paddle_a.ycor() #<-- The (ycor) module returns the Y coordinates of paddle_a
    y +=20 #<-- Will add 20 Pixels to the Y coodinate
    paddle_a.sety(y) #<--- Set the Y to the new Y

def paddle_a_down():
    y = paddle_a.ycor() 
    y -=20 
    paddle_a.sety(y) 

def paddle_b_up():
    y = paddle_b.ycor() 
    y +=20 
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() 
    y -=20 
    paddle_b.sety(y) 

#KeyBoard Binding
makingWindow.listen() #<--This tells it listen for keyboard in puts
makingWindow.onkeypress(paddle_a_up,"w") #<--Its a lowercase w so if capslock on it won't work
makingWindow.onkeypress(paddle_a_down,"s")

makingWindow.onkeypress(paddle_b_up,"Up") #<-- To use the Up Arrow Key
makingWindow.onkeypress(paddle_b_down,"Down") #<-- To use the Down Arrow Key


#Main Gameloop
while True:
    makingWindow.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx) #<--Current X cordinate of the ball cotcatinated with the movement of 2
    ball.sety(ball.ycor() + ball.dy)

    #Boarder Checking <-- What we want the ball to do after hitting the boards. 
    #We ccan do this by comparing the Y coordinates.
    #The Y Axis will rebound the ball 
    if ball.ycor() > 290:
        ball.sety(290) #<--Places the ball at 290 at that specific moment 
        ball.dy *= -1  #It reverses the direction of the ball
        winsound.PlaySound("D:\Coding on Program Languages\Pong\jump-sound-14839.mp3",winsound.SND_ASYNC),winsound.SND_ASYNC
    if ball.ycor() < -290:
        ball.sety(-290)  
        ball.dy *= -1
        winsound.PlaySound("D:\Coding on Program Languages\Pong\jump-sound-14839.mp3",winsound.SND_ASYNC),winsound.SND_ASYNC

    #The X Axis will not rebound the ball
    # It will basically put the ball right in the middle after 
    # hitting it and will make it move in the opposite direction.    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b) ,align="center",font=("Courier", 24 ,"normal" ))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1   
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b) ,align="center",font=("Courier", 24 ,"normal" ))



    #Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("D:\Coding on Program Languages\Pong\jump-sound-14839.mp3",winsound.SND_ASYNC),winsound.SND_ASYNC


    if (ball.xcor() < -340 and ball.xcor() >-350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() >paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1  
        winsound.PlaySound("D:\Coding on Program Languages\Pong\jump-sound-14839.mp3",winsound.SND_ASYNC),winsound.SND_ASYNC




 

