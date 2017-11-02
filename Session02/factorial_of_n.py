print("FACTORIAL OF N!")

n = int(input("Enter n: "))

if n < 0:
    print("Error, n must be >= 0")
else:
    result = 1
    for i in range(1, n + 1):
        result *= i
    print("{0}! = {1}".format(n, result))
