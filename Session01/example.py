# n = int(input("Enter a number: "))
#
# for i in range(n):
#     print (i, end = ' ')
n = int(input("Enter a number: "))
# for i in range (0, n, 2):
#     print(i)

for i in range (n):
    if i%2 == 0:
        print("Fizz")
    elif i%3 == 0:
        print("Buzz")
    elif i%6 ==0:
        print("FizzBuss")
