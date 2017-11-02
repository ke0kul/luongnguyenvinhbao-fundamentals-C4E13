r = int(input("Row(s): "))
c = int(input("Column(s): "))

for i in range(r):
    for j in range (c):
        if i % 2 == 0:
            if j % 2 == 0:
                print("x", end = ' ')
            else:
                print("*", end = ' ')
        else:
            if j % 2 == 0:
                print("*", end = ' ')
            else:
                print("x", end = ' ')
    print()
