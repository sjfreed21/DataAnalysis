#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:48:25 2020

@author: zhwa2432
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    # ydata.append(np.sin(frame))
    ydata.append(np.sin(frame)*np.cos(frame))
    ln.set_data(xdata, ydata)
    return ln,
'''
init()
for frame in np.linspace(0, 2*np.pi, 64):
    print(frame)
    update(frame)
    if (frame > 5.5):
        plt.show()    
'''
    
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 64),
                    init_func=init, blit=True)
ani.save('FuncAnimation_test.gif')

plt.show()