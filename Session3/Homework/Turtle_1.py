colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *

n = int(input("Enter n (3 <= n <= 8): "))
if n >= 3 and n < 10:
    c = -1
    for i in range(3, n):
        c += 1
        pencolor = colors[c]
        color(pencolor)
        for j in range(i):
            forward(100)
            left(360/i)
else:
    print("invalid n!")
mainloop()
