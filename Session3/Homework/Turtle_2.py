colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *

c = -1

for __ in range(len(colors)):
    c += 1
    pen_color = colors[c]
    color(pen_color)
    begin_fill()
    for _ in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    forward(50)
    end_fill()

mainloop()
