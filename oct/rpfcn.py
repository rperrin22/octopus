import segyio
import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd

def plot_seis(filename):
    fseis = segio.open(filename, ignore_geometry=True)

    seis_data = fseis.trace.raw[:]

    plt.imshow(seis_data.T,cmap=plt.cm.bone)
    plt.colorbar()
    plt.grid()
    plt.show()