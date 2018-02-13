"""
Author:    Piotr Masztalski
Created:   12.02.2018

A few useful functions for processing audio
"""

# required packages
import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read as wavread
from soundfile import read


# plot a signal
def plot_wav(filename):
    # reading the wave file
    fs, signal = wavread(filename)

    # creating a time vector
    time = np.linspace(0, len(signal)/fs, num=len(signal))

    # recalcucating the amplitude (range from -1 to 1)
    if signal.dtype == 'int16':
        signal = signal / 2 ** 15
    elif signal.dtype == 'int32':
        signal = signal / 2 ** 31

    # plotting the signal
    plt.figure(1)
    plt.plot(time, signal)
    plt.ylabel("Amplitude")
    plt.xlabel("Time [s]")
    plt.ylim(-1, 1)
    plt.show()


# plot fft of a signal
def plot_fft(filename):
    # another option of reading the signal(no need to recalculate the amplitude)
    signal, fs = read(filename)

    # creating a frequency vector
    freqs = np.arange(-fs/2, fs/2, step=fs/len(signal))

    # computing and shifting the fft of the signal
    my_fft = np.fft.fft(signal)
    my_fft = np.fft.fftshift(my_fft)

    # plotting the fft
    plt.figure(1)
    plt.plot(freqs, abs(my_fft))
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")
    plt.xlim(0, 20000)  # adjusting the frequency axis to the human hearing range
    plt.show()


# plot spectrogram of a signal
def plot_spectrogram(filename):
    signal, fs = read(filename)
    plt.figure(1)
    plt.specgram(signal, Fs=fs)
    plt.ylabel("Frequency [Hz]")
    plt.xlabel("Time [s]")
    plt.ylim(0, 20000)  # adjusting the frequency axis to the human hearing range
    plt.show()