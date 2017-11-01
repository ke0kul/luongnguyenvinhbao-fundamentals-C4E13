print("Hi there, my name is Mr Moody")

from random import randrange

n = randrange(1, 100)
if n < 30:
    print("I'm feeling sad")
elif n < 60:
    print("I'm feeling OK")
else:
    print("Oh yeah, let's rock this world")
