# -*- coding: utf-8 -*-
"""
Created on Mon Feb 09 19:44:39 2015

@author: rahull.sharma
"""

import numpy as np
import matplotlib.pyplot as plt
from math import  pi,e
from plotting import plot
def plotvector():
    ip=[3,2]
    ip1=np.multiply(2,ip)
    print ip1
    soa =np.array( [ip,ip1]) 
    X,Y = zip(*soa)
    plt.figure()
    ax = plt.gca()
    ax.quiver(X,Y,angles='xy',scale_units='xy',scale=1)
    ax.set_xlim([0,10])
    ax.set_ylim([0,10])
    plt.draw()
    plt.show()

def playwithcircle():
    plot(e**(t*pi*1j/20) for t in range(20))    
    print 'test'

playwithcircle
    