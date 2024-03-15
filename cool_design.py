import colorsys
from turtle import *

tracer(500) #helps control turtle
bgcolor('light blue')

def draw():

    for i in range(100):
        
        if i % 2 == 0:
            c = 'white'
        else:
            c = 'black'
        up()
        goto(0,0)
        down()
        color('black')
        fillcolor (c)
        begin_fill()
        rt(98)
        circle(i, 12)
        fd (290)
        fd (i)
        lt (29)
        for j in range(129):
            fd(i)
            circle(j, 299, steps = 2)
        end_fill()

if __name__ == "__main__":
    screen = Screen()
    screen.bgcolor('lightblue')
    screen.setup(width=1.0, height=1.0)
    draw()
    screen.mainloop()  