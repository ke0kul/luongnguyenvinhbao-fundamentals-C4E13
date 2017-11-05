colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *

n = int(input("Nhap n: "))

for i in range(3, n):
    for j in range(i):
        forward(100)
        left(360/i)

mainloop()
