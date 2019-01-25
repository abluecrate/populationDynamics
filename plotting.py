import matplotlib.pyplot as plt
from matplotlib import animation

#-------------------------------------------------------------------------------------------------------------------------------------------

def Plot(population):
    fig, ax = plt.subplots()
    ax1 = plt.axes(xlim = (0, population.cycles + 10), 
                   ylim = (0, max(max(population.prey), max(population.predator)) + 10))
    line, = ax1.plot([], [], lw = 1)
    plt.title('PREDATOR v PREY')
    plt.xlabel('Cycle')
    plt.ylabel('Population')

    plotlays, plotcols = [2], ["orange","blue"]
    lines = []
    for index in range(2):
        lobj = ax1.plot([], [], lw = 2, color = plotcols[index])[0]
        lines.append(lobj)

    def init():
        for line in lines:
            line.set_data([],[])
        return lines

    x1,y1 = [],[]
    x2,y2 = [],[]

    timeData = range(0,population.cycles)
    preyData = population.prey
    predatorData = population.predator

    def animate(i):
        x = timeData[i]
        y = preyData[i]
        x1.append(x)
        y1.append(y)
        x = timeData[i]
        y = predatorData[i]
        x2.append(x)
        y2.append(y)
        xlist = [x1, x2]
        ylist = [y1, y2]

        for lnum, line in enumerate(lines):
            line.set_data(xlist[lnum], ylist[lnum])
        return lines

    frames = population.cycles
    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = frames, repeat = False, interval = 1, blit = True)
    # plt.grid()
    plt.show()

#-------------------------------------------------------------------------------------------------------------------------------------------
