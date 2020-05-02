from random import randint

def genRandomList(size):
    a = []
    for i in range(size):
        n = randint(1,1000)
        a.append(n)
    return a