#-------------------------------------------------------------------------------------------------------------------------------------------

class Population(object):
    def __init__(self, nPrey0, nPredator0, dTime, cycles):
        self.prey = [nPrey0]            # Number of Prey
        self.predator = [nPredator0]    # Number of Predators

        self.preyBR = 0.5           # Prey Birth Rate       
        self.preyDR = 0.015         # Prey Death Rate
        self.predatorBR = 0.015     # Predator Birth Rate
        self.predatorDR = 0.5       # Predator Death Rate

        self.dTime = dTime
        self.cycles = cycles
        # self.timeSpace = range(0,self.cycles)

    def simulate(self):
        for t in range(0, self.cycles):
            nPrey = self.prey[t] + self.dTime*(self.preyBR*self.prey[t] - self.preyDR*self.prey[t]*self.predator[t])
            nPredator = self.predator[t] + self.dTime*(self.predatorBR*self.predator[t]*self.prey[t] - self.predatorDR*self.predator[t])
            self.prey.append(nPrey)
            self.predator.append(nPredator)

#-------------------------------------------------------------------------------------------------------------------------------------------

