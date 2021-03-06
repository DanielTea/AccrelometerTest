import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

import os
dir_path = os.path.dirname(os.path.realpath(__file__))


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = open(dir_path+"/test.txt","r").read()
    dataArray = pullData.split('\n')
    xar = []
    yar = []
    for eachLine in dataArray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            xar.append(int(x))
            yar.append(int(y))
    ax1.clear()
    ax1.plot(xar,yar)


ani = animation.FuncAnimation(fig, animate, interval=10)
plt.show()