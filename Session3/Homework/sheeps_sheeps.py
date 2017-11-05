#2.1.present
print("Hello, my name is Bao and these are my sheep size:")
size = [5, 7, 300, 90, 24, 50, 75]
print(size)

#####create loops


months = int(input("How long do you want to keep them up???? "))
# #2.2.choose the biggest sheep
for i in range (months):

    print("Now my biggest sheep has size {0}, let's shear it!".format(max(size)))

    #2.3.resize the biggest
    size[(size.index(max(size)))] = 8
    print("After shearing, here is my flock:")
    print(size)

    #2.4. Increasing size after one month.
    for j in range ( len (size) ):
        size [j] += 50
    print("Month(s) has passed, now here is my flock:")
    print(size)

    #2.5.
    print("My flock has size in total", sum(size))
    print("I would get {0} * 2$ = {1}$".format(sum(size),sum(size)*2))
