import segyio
import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd

def plot_seis(filename):
    fseis = segyio.open(filename, ignore_geometry=True)

    seis_data = fseis.trace.raw[:]

    fseis.close()

    plt.imshow(seis_data.T,cmap=plt.cm.bone,aspect=5)
    plt.colorbar()
    plt.grid()
    plt.show()

def print_ebcdic(filename):
    fseis = segyio.open(filename, ignore_geometry=True)

    print(fseis.text)

    fseis.close()