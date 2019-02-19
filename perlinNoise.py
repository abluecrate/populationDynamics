import numpy as np
import matplotlib.pyplot as plt

def getGradient(seed):
    seed and np.random.seed(seed)
    gradient = np.random.rand(512, 512, 2) * 2 - 1
    return gradient

def fade(values):
    return 6*values**5 - 15*values**4 + 10*values**3

def perlin_noise(sizeX, sizeY, frequency,seed = None):
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

    return g

print('-----------------------------------------------------------------')

seed = None
map = perlin_noise(64, 64, 4, seed)

print(map.shape)

print('-----------------------------------------------------------------')

fig, ax = plt.subplots()
ax.matshow(map, cmap = plt.cm.Blues)
plt.show()

