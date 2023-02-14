from turtle import *

def square(d=200):
    for i in range(4):
        fd(d)
        lt(90)
    
def polygon(side=3,dis=50):
    for i in range(side):
        fd(dis)
        lt(360/side)

polygon()
hideturtle()
mainloop() 