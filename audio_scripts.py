'''
Author:    Piotr Masztalski
Created:   12.02.2018
'''

import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read as wavread


def plot_wav(filename):
    #reading the wave file
    fs, signal = wavread(filename)

    #creating a time vector
    time = np.linspace(0, len(signal)/fs, num=len(signal))

    #recalcucating the amplitude (range from -1 to 1)
    if signal.dtype == 'int16':
        bits = 16
    elif signal.dtype == 'int32':
        bits = 32
    signal = signal/2**(bits - 1)

    #plotting the signal
    plt.figure(1)
    plt.plot(time, signal)
    plt.ylabel("Amplitude")
    plt.xlabel("Time [s]")
    plt.ylim(-1, 1)
    plt.show()






