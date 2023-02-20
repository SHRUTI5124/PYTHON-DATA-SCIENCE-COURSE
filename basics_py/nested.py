from turtle import *
speed(0)

fillcolor("pink")
pencolor("black")

side=6
for i in range(side):
    fd(100)
    for i in range(side):
        fd(50)
        begin_fill()
        for i in range(side):
            fd(25)
            dot(10)
            rt(360/side)
        end_fill()
        lt(360/side)
    rt(360/side)

hideturtle()
mainloop()