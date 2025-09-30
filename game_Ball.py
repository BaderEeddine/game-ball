import turtle


# Create a screen shape
win = turtle.Screen()
win.bgcolor("black")
win.setup(width=800, height=600) 
win.title("Game Ball")
win.tracer(0)

# Create a menu turtle
menuo = turtle.Turtle()
menuo.color("white")
menuo.penup()
menuo.hideturtle()
menuo.goto(0, 50)
menuo.write("Press Enter to start the game.", align = "center",font = ('Courier', 25, "bold"))

menuo.goto(0, -20)
menuo.write("Press Q to exit.", align = "center",font = ('Courier', 18, "normal"))

# Display instructions
menuo.goto(0, -120)
menuo.color('red')
menuo.penup()
menuo.write("Read the instructions.", align = "center",font = ('Courier', 20, "bold"))


menuo.goto(0, -160)
menuo.color("green")
menuo.penup()
menuo.write("Must be played by two people.", align = "center",font = ('Courier', 18, "normal"))

menuo.goto(0, -190)
menuo.color("green")
menuo.penup()
menuo.write("normal control.", align = "center",font = ('Courier', 18, "normal"))


def menuo_q():
    turtle.bye()


def menuo_run():
    menuo.clear()
    run_game()

win.listen()
win.onkeypress(menuo_run, "Return")
win.onkeypress(menuo_q, "q")


def run_game():
    win.clear()
    win.bgcolor('black')
    win.tracer(0)

    #Create a mdrb1 form
    mdrb1 = turtle.Turtle()
    mdrb1.speed(0)
    mdrb1.shape("square")
    mdrb1.color("red")
    mdrb1.penup()
    mdrb1.goto(350, 0)
    mdrb1.shapesize(stretch_wid = 5, stretch_len = 1)
    mdrb1.dy = 2.0
    mdrb1.dx = 2.0

    #Create a mdrb2 form
    mdrb2 = turtle.Turtle()
    mdrb2.speed(0)
    mdrb2.shape("square")
    mdrb2.color("blue")
    mdrb2.penup()
    mdrb2.goto(-350, 0)
    mdrb2.shapesize(stretch_wid = 5, stretch_len = 1)

    #Create ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.5
    ball.dy = 0.5

    #scoure
    scoure = turtle.Turtle()
    scoure.speed(0)
    scoure.color("white")
    scoure.penup()
    scoure.goto(0, 260)
    scoure.hideturtle()
    scoure.goto(0, 260)
    scoure.write("player1 : 0   player2 : 0 ", align = "center",font = ("Arial", 20, "normal"))
    scoure1 = 0
    scoure2 = 0


    #Control mdrb1
    def mdrb_up_1():
        y = mdrb1.ycor()
        y += 30
        mdrb1.sety(y)

    def mdrb_dwn_1():
        y = mdrb1.ycor()
        y -= 30
        mdrb1.sety(y)

    #Control mdrb2
    def mdrb_up_2():
        y = mdrb2.ycor()
        y += 30
        mdrb2.sety(y)

    def mdrb_dwn_2():
        y = mdrb2.ycor()
        y -= 30
        mdrb2.sety(y)


    win.listen()
    win.onkeypress(mdrb_up_1, "Up")
    win.onkeypress(mdrb_dwn_1, "Down")
    win.onkeypress(mdrb_up_2, "w")
    win.onkeypress(mdrb_dwn_2, "s")



    while True:
        win.update()

        # جعل الكرة تتحرك
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        #الى خرجات الكرة خصها ترجع
        if ball.xcor() > 390:
            ball.setx(390)
            ball.goto(0, 0)
            ball.dx *= -1
            scoure.clear()
            scoure1 += 1
            scoure.write("player1 : {}   player2 : {} ".format(scoure1, scoure2), align="center", font=("Arial", 20, "normal"))

        if ball.xcor() < -390:
            ball.setx(-390)
            ball.goto(0, 0)
            ball.dx *= -1
            scoure.clear()
            scoure2 += 1
            scoure.write("player1 : {}    player2 : {} ".format(scoure1, scoure2), align="center",font=("Arial", 20, "normal"))

            #الى الكرة دربتا في المدرب خسها ترتد
        if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < mdrb1.ycor() +60 and ball.ycor() > mdrb1.ycor() -60):
            ball.setx(340)
            ball.dx *= -1

        if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < mdrb2.ycor() +60 and ball.ycor() > mdrb2.ycor() -60):
            ball.setx(-340)
            ball.dx *= -1

        # Fix screen border penetration issue
        if mdrb1.ycor() > 250 and mdrb1.ycor() < 300:
            mdrb1.sety(250)

        if mdrb1.ycor() < -250 and mdrb1.ycor() > -300:
            mdrb1.sety(-250)




        if mdrb2.ycor() > 250 and mdrb2.ycor() < 300:
            mdrb2.sety(250)

        if mdrb2.ycor() < -250 and mdrb2.ycor() > -300:
            mdrb2.sety(-250)


        win.onkeypress(menuo_q, "q")

win.mainloop()