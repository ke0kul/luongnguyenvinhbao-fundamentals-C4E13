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
