import random
import numpy as np
import matplotlib.pyplot as plt

def genNoise(mHeight, mWidth):
    noiseMap = []
    for _ in range(mHeight):
        newRow = []
        for _ in range(mWidth):
            newRow.append(0)
        noiseMap.append(newRow)
    
    newValue = 0
    topRange = 0
    bottomRange = 0

    for y in range(mHeight):
        for x in range(mWidth):
            if x ==0 and y == 0:
                continue
            if y == 0:
                newValue = noiseMap[y][x-1] + random.randint(-1000,1000)
            elif x == 0:
                newValue = noiseMap[y-1][x] + random.randint(-1000,1000)
            else:
                minimum = min(noiseMap[y][x-1],noiseMap[y-1][x])
                maximum = max(noiseMap[y][x-1],noiseMap[y-1][x])
                avgVal = minimum + ((maximum - minimum)/2)
                newValue = avgVal + random.randint(-1000,1000)
            noiseMap[y][x] = newValue

            if newValue < bottomRange:
                bottomRange = newValue
            elif newValue > topRange:
                topRange = newValue
    
    diff = float(topRange - bottomRange)
    for y in range(mHeight):
        for x in range(mWidth):
            noiseMap[y][x] = (noiseMap[y][x] - bottomRange)/diff

    return noiseMap

map = genNoise(100,100)

fig, ax = plt.subplots()
ax.matshow(map, cmap = plt.cm.Blues)
plt.show()

# REFERENCES

# https://medium.com/inspired-to-program-%E3%85%82-%D9%88-%CC%91%CC%91/procedural-generation-in-python-7b75127b2f74
# http://www.roguebasin.com/index.php?title=Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels
# https://stackoverflow.com/questions/17779480/python-random-map-generation-with-perlin-noise