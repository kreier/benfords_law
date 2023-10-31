# inspiration: https://youtu.be/sf5OrthVRPA?si=5NKcP-MENOteJrKH&t=2211 32:18
# source from comment @nicksdrumsticks

import random

cards = [i for i in range(52)]

def hasNextToOrOneApart(kings, queens):
    for king in kings:
        for queen in queens:
            if king == queen - 1 or king == queen + 1 or king == queen - 2 or king == queen + 2:
                return True
    return False

def discoverNewPack():
    topEight = random.sample(cards, k=8)
    kings, queens = topEight[:4], topEight[4:8]
    return hasNextToOrOneApart(kings, queens)

count = 0
numIterations = 1000000

for _ in range(numIterations):
    count += discoverNewPack()

print(count / numIterations)
