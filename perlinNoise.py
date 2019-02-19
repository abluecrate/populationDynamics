import numpy as np
import matplotlib.pyplot as plt


def getGradient(seed):
    seed and np.random.seed(seed)
    gradient = np.random.rand(512, 512, 2) * 2 - 1
    return gradient

def fade(values):
    return 6*values**5 - 15*values**4 + 10*values**3

def perlin_noise(sizeX, sizeY, frequency, seed = None):
    gradient = getGradient(seed)
    
    x = np.tile(np.linspace(0, frequency, sizeX, endpoint = False), sizeY)
    x = x.reshape(sizeX, sizeY)
    y = np.repeat( np.linspace(0, frequency, sizeY, endpoint = False), sizeX)
    y = y.reshape(sizeX, sizeY)

    x0 = x.astype(int)
    x -= x0
    y0 = y.astype(int)
    y -= y0

    g00 = gradient[x0, y0]
    g10 = gradient[x0 + 1, y0]
    g01 = gradient[x0, y0 + 1]
    g11 = gradient[x0 + 1, y0 + 1]

    fadeX = fade(x)

    q1 = g00[:,:,0] * x + g00[:,:,1] * y
    q2 = g10[:,:,0] * (x - 1) + g10[:,:,1] * y
    g0 = q1 + fadeX * (q2 - q1)

    q3 = g01[:,:,0] * x + g01[:,:,1] * (y - 1)
    q4 = g11[:,:,0] * (x - 1) + g11[:,:,1] * (y - 1)
    g1 = q3 + fadeX * (q4 - q3)

    fadeY = fade(y)

    g = g0 + fadeY * (g1 - g0)

    max = np.amax(g)
    min = np.amin(g)

    return (g - min) / (max - min)

def calculateCircleGradient(mapArray):
    sizeX, sizeY = mapArray.shape
    x = np.tile(np.linspace(0, sizeX, sizeX, endpoint = False), sizeY)
    x = x.reshape(sizeX, sizeY)
    y = np.repeat( np.linspace(0, sizeY, sizeY, endpoint = False), sizeX)
    y = y.reshape(sizeX, sizeY)

    centerPointX = sizeX/2
    centerPointY = sizeY/2

    distanceFromCenter = abs(np.sqrt((x - centerPointX)**2+ (y - centerPointY)**2) - np.mean([sizeX,sizeY]))

    max = np.amax(distanceFromCenter)
    min = np.amin(distanceFromCenter)

    # oGrid = np.ogrid[0:mapArray.shape[0], 0:mapArray.shape[1]]
    # centerPoint = np.array(centerPoint).astype(int)
    # distanceFromCenter = np.sqrt(((np.argwhere(mapArray > 0) - centerPoint)**2).sum(1)).mean()
    # distanceFromCenter = cdist(mapArray, np.atleast_2d(centerPoint)).ravel()
    # distanceFromCenter = np.sqrt(((oGrid - centerPoint)**2).sum(1)).mean()

    return (distanceFromCenter - min) / (max - min)

print('-----------------------------------------------------------------')

seed = None

noiseMap = perlin_noise(128, 128, 4, seed)

# moistureMap = perlin_noise(64, 64, 2)

circleGradient = calculateCircleGradient(noiseMap)

map = noiseMap * circleGradient

print('-----------------------------------------------------------------')

fig, (ax1, ax2, ax3) = plt.subplots(1,3)
ax1.matshow(noiseMap, cmap = plt.cm.Greys)
ax2.matshow(circleGradient, cmap = plt.cm.Greys)
ax3.matshow(map, cmap = plt.cm.terrain)
plt.show()

