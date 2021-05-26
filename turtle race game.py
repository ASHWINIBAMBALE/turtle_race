from turtle import Turtle, Screen
import random
tim=Turtle()
screen=Screen()
is_race_on=False
all_Turtle=[]
user_bet=screen.textinput("make your bets:","which turtle will win ? enter the color:")
print(user_bet)
colors=["red","orange","black","green","yellow","blue"]
screen.setup(width=700,height=700)
y_position=[-70,-40,-10,20,50,80]
for i in range(0,6):
    tim=Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-250,y=y_position[i])
    all_Turtle.append(tim)
if user_bet:
    is_race_on=True
while is_race_on:
    for i in all_Turtle:
        if i.xcor() > 230:
            is_race_on=False
            wining_color = i.pencolor()
            if user_bet==wining_color:
                print(f"You won! The color of wining turtle is {wining_color} ")
            else:
                print(f"You lose! The color of wining turtle is {wining_color}")
        rand_distance=random.randint(0,10)
        i.forward(rand_distance)
screen.exitonclick()