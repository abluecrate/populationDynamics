import numpy as np
import matplotlib.pyplot as plt

import argparse
import time

#------------------------------------------------------------------------------------------------
#################################################################################################
#------------------------------------------------------------------------------------------------

# class Board(object):
#     def __init__(self, size, seed = 'Random'):
#         if seed == 'Random':
#             self.state = np.random.randint(2, size = size)
#         self.engine = Engine(self)
#         self.iteration = 0

#     def animate(self):
#         i = self.iteration
#         im = None
#         plt.title("Conway's Game of Life")
#         while True:
#             if i == 0:
#                 plt.ion()
#                 im = plt.imshow(self.state, vmin = 0, vmax = 2)
#             else:
#                 im.set_data(self.state)
#             i += 1
#             self.engine.applyRules()
#             # print('Life Cycle:  {}    Birth:  {}    Survive:  {}'.format(i, self.engine.nBirth, self.engine.nSurvive))
#             plt.pause(0.01)
#             yield self

#------------------------------------------------------------------------------------------------
#################################################################################################
#------------------------------------------------------------------------------------------------

class Population(object):
    def __init__(self, sizeX, sizeY, populationType, seed = None):
        # if seed == 'Random':
        #     self.state = np.random.randint(2, size = size)
        self.size = (sizeY, sizeX)
        seed and np.random.seed(seed)
        self.state = np.random.randint(2, size = self.size)
        self.populationType = populationType
        self.engine = Engine(self)
        # self.iteration = 0

#------------------------------------------------------------------------------------------------
#################################################################################################
#------------------------------------------------------------------------------------------------

class Map(object):
    def __init__(self, sizeX, sizeY, seed = None):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.seed = seed

        landMap, landIndex = self.generateIsland()

        self.landMap = landMap
        self.landIndex = landIndex

    def getGradient(self):
        self.seed and np.random.seed(self.seed)
        gradient = np.random.rand(512, 512, 2) * 2 - 1
        return gradient

    def fade(self, values):
        return 6*values**5 - 15*values**4 + 10*values**3

    def perlinNoise(self, frequency):

        gradient = self.getGradient()
        
        x = np.tile(np.linspace(0, frequency, self.sizeX, endpoint = False), self.sizeY)
        x = x.reshape(self.sizeX, self.sizeY)
        y = np.repeat( np.linspace(0, frequency, self.sizeY, endpoint = False), self.sizeX)
        y = y.reshape(self.sizeX, self.sizeY)

        x0 = x.astype(int)
        x -= x0
        y0 = y.astype(int)
        y -= y0

        g00 = gradient[x0, y0]
        g10 = gradient[x0 + 1, y0]
        g01 = gradient[x0, y0 + 1]
        g11 = gradient[x0 + 1, y0 + 1]

        fadeX = self.fade(x)

        q1 = g00[:,:,0] * x + g00[:,:,1] * y
        q2 = g10[:,:,0] * (x - 1) + g10[:,:,1] * y
        g0 = q1 + fadeX * (q2 - q1)

        q3 = g01[:,:,0] * x + g01[:,:,1] * (y - 1)
        q4 = g11[:,:,0] * (x - 1) + g11[:,:,1] * (y - 1)
        g1 = q3 + fadeX * (q4 - q3)

        fadeY = self.fade(y)

        g = g0 + fadeY * (g1 - g0)

        mx = np.amax(g)
        mn = np.amin(g)

        return (g - mn) / (mx - mn)

    def calculateCircleGradient(self):
        x = np.tile(np.linspace(0, self.sizeX, self.sizeX, endpoint = False), self.sizeY)
        x = x.reshape(self.sizeX, self.sizeY)
        y = np.repeat( np.linspace(0, self.sizeY, self.sizeY, endpoint = False), self.sizeX)
        y = y.reshape(self.sizeX, self.sizeY)

        centerPointX = self.sizeX/2 
        centerPointY = self.sizeY/2

        distanceFromCenter = abs(np.sqrt((x - centerPointX)**2+ (y - centerPointY)**2) - np.mean([self.sizeX,self.sizeY]))

        mx = np.amax(distanceFromCenter)
        mn = np.amin(distanceFromCenter)

        return ((distanceFromCenter - mn) / (mx - mn))**2

    def generateIsland(self):
        noiseMap = self.perlinNoise(4)
        # moistureMap = perlin_noise(64, 64, 2)
        circleGradient = self.calculateCircleGradient()
        landMap = noiseMap * circleGradient
        landIndex = landMap >= 0.115

        return landMap, landIndex

#------------------------------------------------------------------------------------------------
#################################################################################################
#------------------------------------------------------------------------------------------------

class Engine(object):
    def __init__(self, population):
        self.state = population.state
        self.populationType = population.populationType

    def countNeighbors(self):
        state = self.state
        n = (state[0:-2,0:-2] + state[0:-2,1:-1] + state[0:-2,2:] +
             state[1:-1,0:-2] + state[1:-1,2:] + state[2:,0:-2] +
             state[2:,1:-1] + state[2:,2:])
        return n   

    # def applyRules(self):
        # if self.populationType == 'Prey':
        #     state = self.preyRules()
        # elif self.populationType == 'Predator':
        #     state = self.predatorRules()
        # elif self.populationType == 'Plant':
        #     state = self.plantRules()
        # return state

    # def preyRules(self):
        # n = self.countNeighbors() 
        # state = self.state

        # birth = (n == 3) & (state[1:-1,1:-1] == 0)
        # survive = ((n == 2) | (n == 3)) & (state[1:-1,1:-1] == 1)
        # state[...] = 0
        # state[1:-1,1:-1][birth | survive] = 1

        # nBirth = np.sum(birth)
        # self.nBirth = nBirth
        # nSurvive = np.sum(survive)
        # self.nSurvive = nSurvive

        # return state

    # def predatorRules(self):
        # n = self.countNeighbors() 
        # state = self.state

        # birth = (n == 3) & (state[1:-1,1:-1] == 0)
        # survive = ((n == 2) | (n == 3)) & (state[1:-1,1:-1] == 1)
        # state[...] = 0
        # state[1:-1,1:-1][birth | survive] = 1

        # nBirth = np.sum(birth)
        # self.nBirth = nBirth
        # nSurvive = np.sum(survive)
        # self.nSurvive = nSurvive

        # return state

    # def plantRules(self):
        # n = self.countNeighbors() 
        # state = self.state
        

#------------------------------------------------------------------------------------------------
#################################################################################################
#------------------------------------------------------------------------------------------------

def main():

    # ap = argparse.ArgumentParser(add_help = False)  # Intilialize Argument Parser
    # ap.add_argument('-h', '--height', help = 'Board Height', default = 256)
    # ap.add_argument('-w', '--width', help = 'Board Width', default = 256)
    # args = vars(ap.parse_args())    # Gather Arguments

    # bHeight = int(args['height'])
    # bWidth = int(args['width'])

    # board = Board()
    # for _ in board.animate():
    #     pass

    mapX = 256
    mapY = 256

    island = Map(mapX, mapY)

    prey = Population(mapX, mapY, 'Prey')
    predators = Population(mapX, mapY, 'Predator')
    plants = Population(mapX, mapY, 'Plant')

    # fig, (ax1, ax2, ax3) = plt.subplots(1,3)
    # ax1.matshow(prey.state)
    # ax2.matshow(predators.state)
    # ax3.matshow(plants.state)
    # plt.show()

    # plt.close('all')
    # fig, (ax1, ax2) = plt.subplots(1,2)
    # ax1.matshow(test.landMap)
    # ax2.matshow(test.landIndex)

    # ax1.matshow(noiseMap, cmap = plt.cm.Greys)
    # ax2.matshow(circleGradient, cmap = plt.cm.Greys)
    # ax3.matshow(map, cmap = plt.cm.terrain)
    # ax4.matshow(landMap, cmap = plt.cm.terrain)
    
    # plt.show()

#------------------------------------------------------------------------------------------------
#################################################################################################
#------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    main()