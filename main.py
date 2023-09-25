import matplotlib.pyplot as plt
import matplotlib.animation as anim
import numpy as np
from random import uniform

def circle():
    T = np.arange(0,2*np.pi, 0.001)
    X = []
    Y = [] 
    for t in T:
        X.append(np.cos(t))
        Y.append(np.sin(t))
    fig, ax = plt.subplots()
    ax.plot(X,Y, 'r-', linewidth=2)
    ax.set(xlim=(-1,1), ylim=(-1,1))
    return fig, ax

def throw_dart():
    x = uniform(-1,1)
    y = uniform(-1,1)
    plt.scatter(x,y)
    return (x,y)

def main(darts):
    fig, ax = circle()
    fig.suptitle("Plot with %d darts"%darts, fontsize=14, fontweight='bold')
    n=0
    count = 0
    while n<darts:
        (x,y) = throw_dart()
        if x**2 + y**2 <= 1:
            count+=1
        pi = 4*(count/(n+1))
        ax.set_title("Our estimate of pi is %3.2f"%pi)
        plt.pause(0.0005)
        n+=1
    plt.show()

main(500)
