import random
import turtle
from turtle import Turtle

# turtle.colormode(255)
screen = turtle.Screen()
turtle.title("Turtle race")
screen.setup(width=700, height=600)
colors = ["red","green","black","yellow","blue","orange"]
y_position = [0,-85,-170,-255,85,170]
play_on = True




def track():
    screen.clear()
    all_turtles =[]
    all_turtles.clear()
    n = 6
    for turtles in range(6):
        new_turtle: Turtle = turtle.Turtle()
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.color(colors[turtles])
        if turtles == n-1:
            new_turtle.goto(x=320,y=260)
            new_turtle.right(90)
            new_turtle.pendown()
            new_turtle.forward(520)
            new_turtle.penup()
            new_turtle.left(90)
        new_turtle.goto(x=-320 , y=y_position[turtles])
        all_turtles.append(new_turtle)
    run(turtle_list=all_turtles)
def run(turtle_list):
    global is_race_on
    user_bet = screen.textinput(title="race",prompt="which colour do you bet on").lower()
    if user_bet:
        is_race_on = True
    while play_on:
        while is_race_on:
            for racer in turtle_list:
                if racer.xcor() > 300:
                    winner = racer.pencolor()
                    if user_bet == winner:
                        print("you got it right ")

                    else:
                        print(f"winner is {winner}, better luck next time ")

                    status = screen.textinput(title=f"winner{winner} : ",prompt="do you want to play again (y/n)").lower()

                    if status:
                        if status == "y":
                            track()
                        else:
                            return 0


                racer.forward(random.randint(1,10))


track()



















screen.listen()
# screen.onkey(fun=on_clik , key= "space")

screen.exitonclick()


