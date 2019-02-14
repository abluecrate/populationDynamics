import numpy as np
import matplotlib.pyplot as plt

mapSize = (64,64)
n = np.random.randint(11, size = mapSize) / 10
n = np.gradient(n)
im = plt.imshow(n)
# im.set_cmap('hot')
plt.show()
