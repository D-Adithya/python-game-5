import turtle
from turtle import Turtle,Screen
import pandas as pd
score_list=[]
chance=0
data=pd.read_csv("50_states.csv")
state_list=data['state'].to_list()
x_cor=data['x'].to_list()
y_cor=data['y'].to_list()
screen=Screen()
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while chance<50:
    score=len(score_list)
    answer=screen.textinput(title=f"{score}/50 correct",prompt="whats another state name?")
    answer=answer.title()
    if answer=="Exit":
        missing=[state for state in state_list if state not in score_list]
        # for state in state_list:
        #     if state not in score_list:
        #         missing.append(state)
        print(missing)
        new=pd.DataFrame(missing)
        new.to_csv("missing_states.csv")
        break
    for i in range(len(state_list)):
        if state_list[i]==answer:
            score_list.append(answer)
            tim = Turtle()
            tim.hideturtle()
            tim.penup()
            tim.goto(x=x_cor[i],y=y_cor[i])
            tim.write(f"{answer}",font=('Arial', 10, 'normal'))

    chance+=1
    if chance==50:
        tim=Turtle()
        tim.hideturtle()
        tim.write(f"your score is {score}",font=('Arial', 20, 'normal'))
        game=False

