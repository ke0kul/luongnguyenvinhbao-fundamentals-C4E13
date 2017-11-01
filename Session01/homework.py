#tính chu vi, diện tích hình tròn


import math

R = float(input("Nhập bán kính đường tròn:"))
if R < 0:
    print("Lỗi, đường kính nhỏ hơn 0")
else:
    DV = input("Nhập đơn vị tính (mm/cm/dm/m....):")
    DT = round(math.pi * R * R,3)
    CV = round(2 * math.pi * R,3)
    print("Diện tích hình tròn là: {0} {1}^2".format(DT,DV))
    print("Chu vi hình tròn là: {0} {1}".format(CV,DV))



#chuyển đổi độ C và độ F
C = float(input("Enter the temperature in Celcius?"))
F = (C * 9 / 5) + 32
print("{0} (C) = {1} (F)".format(C,F))


# vẽ hình linh tinh các loại

# vẽ hình vuông
from turtle import *

speed(-1)

for i in range(4):
    forward(100)
    left(90)

mainloop()

# vẽ hình tam giác

from turtle import *

speed(-1)

for i in range(3):
    forward(100)
    left(120)

mainloop()

# ve hinh tron

from turtle import *

speed (-1)
