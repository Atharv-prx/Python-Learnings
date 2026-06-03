from tkinter import *
from Images.Ball import *
import time
import os

window = Tk()

HEIGHT = 500
WIDTH = 500

canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

ball_1 = ball(canvas, 0, 0, 100, 1, 1, "White")
tennis_ball = ball(canvas,0,0,50,4,3,"yellow")
basket_ball = ball(canvas,0,0,125,3,5,"orange")
bowling_ball = ball(canvas,0,0,75,2,1,"black")

while True:
    ball_1.move()
    tennis_ball.move()
    basket_ball.move()
    bowling_ball.move()
    window.update()
    
    time.sleep(0.01)

window.mainloop()