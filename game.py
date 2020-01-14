import turtle
import os
from playsound import playsound
import random

#sound arrays
gretaMad = ['wav/how_dare_you.wav', 'wav/stolen_dreams.wav', 'wav/your_failing_us.wav', 'wav/YEAHH.wav', 'wav/YEAHHHH.wav', 'wav/OK.wav']
lilJonMad = ['wav/WHAT.wav', 'wav/WHATTT.wav', 'wav/WASHAPPENIN.wav', 'wav/future_gen.wav', 'wav/OK.wav']

#screen
wn = turtle.Screen()
wn.title("JW Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# left paddle
lPad = turtle.Turtle()
lPad.speed(0)
lPad.shape("square")
lPad.color("green")
lPad.shapesize(stretch_wid=5, stretch_len=1)
lPad.penup()
lPad.goto(-350, 0)

# right paddle
rPad = turtle.Turtle()
rPad.speed(0)
rPad.shape("square")
rPad.color("green")
rPad.shapesize(stretch_wid=5, stretch_len=1)
rPad.penup()
rPad.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = .5
ball.dy = .5

# score
score_a = 0
score_b = 0
sb = turtle.Turtle()
sb.speed(0)
sb.color("white")
sb.penup()
sb.hideturtle()
sb.goto(0, 250)
sb.write("Lil Jon: {} Greta: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

# funcs
def lPad_up():
    y = lPad.ycor()
    y += 20
    lPad.sety(y)

def lPad_down():
    y = lPad.ycor()
    y -= 20
    lPad.sety(y)

def rPad_up():
    y = rPad.ycor()
    y += 20
    rPad.sety(y)

def rPad_down():
    y = rPad.ycor()
    y -= 20
    rPad.sety(y)

# keyboard binding
wn.listen()
wn.onkeypress(lPad_up, "w")
wn.onkeypress(lPad_down, "s")

wn.onkeypress(rPad_up, "Up")
wn.onkeypress(rPad_down, "Down")

# Main game loop
while True:
    wn.update()

    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

       #left Score
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        sb.clear()
        sb.write("Lil Jon: {} Greta: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        playsound(random.choice(gretaMad), False)
        if score_a == 5:
            winner = "Lil Jon"
            sb.clear()
            wn.addshape('img/liljon3.gif')
            lj = turtle.Turtle()
            lj.shape("img/liljon3.gif")
            lj.shapesize(stretch_wid=1, stretch_len=1)
            lj.goto(0, 0)
            sb.write("{} Wins!!".format(winner), align="center", font=("Courier", 36, "normal"))
            wn.update()
            playsound("wav/TURNDOWNFORWHAT.wav")
            break

        #right Score
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        sb.clear()
        sb.write("Lil Jon: {} Greta: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        playsound(random.choice(lilJonMad), False)
        if score_b == 5:
            winner = "Greta"
            sb.clear()
            wn.addshape('img/greta.gif')
            greta = turtle.Turtle()
            greta.shape("img/greta.gif")
            greta.goto(0, 0)
            sb.write("{} Wins!!".format(winner), align="center", font=("Courier", 36, "normal"))
            wn.update()
            playsound("wav/evil.wav")
            break

    #paddle ball collision
    if (ball.xcor() > 340  and ball.xcor() < 350) and (ball.ycor() < rPad.ycor() + 50 and ball.ycor() > rPad.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < lPad.ycor() + 50 and ball.ycor() > lPad.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1



