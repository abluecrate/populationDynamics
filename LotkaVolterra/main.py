import random

import matplotlib.pyplot as plt
import matplotlib.animation as animation

from population import Population
from plotting import AnimatedPlot

#-------------------------------------------------------------------------------------------------------------------------------------------

def run():

    nPrey0 = random.randint(1,101)
    nPredator0 = random.randint(1,101)
    population = Population(nPrey0, nPredator0, 0.01, 10000)
    population.simulate('LotkaVolterra')
    
    print('--------------------------------------------------------------------')
    print('PREY:')
    print('Start:  {}   End:  {}'.format(population.prey[0],round(population.prey[-1])))
    print('PREDATORS:')
    print('Start:  {}   End:  {}'.format(population.predator[0],round(population.predator[-1])))
    print('--------------------------------------------------------------------')

    AnimatedPlot(population)

#-------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
   run()

#-------------------------------------------------------------------------------------------------------------------------------------------
# NOTES:
#-------------------------------------------------------------------------------------------------------------------------------------------

# Lotka-Volterra Equations:
# x = Number of Prey, y = Number of Predators
# alpha, beta, delta, gamma = Interaction Coefficients
# dx/dt = (alpha)*x - (beta)*x*y
# dy/dt = (delta)*x*y - (gamma)*y

# nEntities = nEntities0 + nBirths - nDeaths + nImmigrants - nMigrants 

#-------------------------------------------------------------------------------------------------------------------------------------------
# REFERENCES
#-------------------------------------------------------------------------------------------------------------------------------------------

# Population Dynamics
# http://tbb.bio.uu.nl/rdb/books.html
# https://nrich.maths.org/7252
# https://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equations
# https://www.digitalbiologist.com/blog/2018/9/a-population-dynamics-model-in-five-lines-of-python
#
# Animating Lines
# https://stackoverflow.com/questions/28074461/animating-growing-line-plot-in-python-matplotlib
# https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/