import segyio
import numpy as np 
from matplotlib import pyplot as plt
import pandas as pd

def plot_seis(filename,aspect_ratio):
    fseis = segyio.open(filename, ignore_geometry=True)

    seis_data = fseis.trace.raw[:]

    fseis.close()

    plt.imshow(seis_data.T,cmap=plt.cm.bone,aspect=aspect_ratio)
    plt.colorbar()
    plt.grid()
    plt.show()

def print_ebcdic(filename):
    fseis = segyio.open(filename, ignore_geometry=True)

    print(fseis.text)

    fseis.close()

def plot_seis_locs(filename,mult):

    groupX = fseis.attributes(segyio.TraceField.GroupX)[:]*mult
    groupY = fseis.attributes(segyio.TraceField.GroupY)[:]*mult

    plt.figure(figsize=(10,10))
    plt.plot(groupX,groupY)
    plt.grid()
    plt.xlabel('Easting (m)')
    plt.ylabel('Northing (m)')
    plt.show()