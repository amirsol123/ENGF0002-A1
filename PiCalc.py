import random


def getLength():
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    length = (((x-0.5)**2)+((y-0.5)**2))**0.5
    if length <= 0.5:
        return True

def estimatePi():
    hits = 0
    total = 1000000
    for i in range(total):
        if getLength() == True:
            hits+=1
    return hits*4/total
print (estimatePi())