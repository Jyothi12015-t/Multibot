from turtle import*
from freegames import square,vector
from random import randrange
import turtle

egg=vector(0,0)
snake=[vector(-10,0)]
aim=vector(0,-10)

def target(x,y):
    aim.x=x
    aim.y=y

def border(head):  
    return -150<head.x<140 and -150<head.y<140

def reaching():
    head=snake[-1].copy()
    head.move(aim)
    if not border(head) or head in snake:
        square(head.x,head.y,10,"black")
        print("Game_Over")
        print("Score ::",(len(snake)-1)*10)
        return 
    snake.append(head)
    if egg==head :
        egg.x=randrange(-15,15)*10
        egg.y=randrange(-15,15)*10
    else:
        snake.pop(0)
    clear()
    for body in snake:
        square(body.x,body.y,10,"red")

    square(egg.x,egg.y,10,"green")
    ontimer(reaching,200)
tracer(False)
listen()
onkey(lambda: target(10, 0), 'Right')
onkey(lambda: target(-10, 0), 'Left')
onkey(lambda: target(0, 10), 'Up')
onkey(lambda: target(0, -10), 'Down')
reaching()
done()





