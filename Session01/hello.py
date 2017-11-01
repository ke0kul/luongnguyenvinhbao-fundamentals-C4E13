# n = input("What's your name?")
# yob = int(input("Your year of birth?"))
# age = 2017 - yob
# print("Hello", n, ", Nam nay ban", age, "tuoi.")
#
# if age < 10:
#     print("Baby")
# elif age < 18:
#     print("Teenager")
# else:
#     print("Adult")
#
# print("ByeBye")
print("Giai phuong trinh bac hai")
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))
delta = b ** 2 - 4 * a * c

if a == 0:
    print("x=",-c/b)
else:
    if delta < 0:
        print("Vo nghiem")
    elif delta == 0:
        print("Nghiem kep, x = ", - b / 2 / a )
    else:
        print("Phuong trinh co 2 nghiem")
        print("x1 =", (-b+delta**0.5)/2/a)
        print("x2 =", (-b-delta**0.5)/2/a)
        print("Phuong trinh co 2 nghiem, x1={0}, x2={1}".format(x1, x2))
