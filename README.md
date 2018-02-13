# Audio Processing Scripts
Functions that let you:
* Plot a signal
* Plot FFT of a signal
* Plot a spectrogram of a signal
Code provided in the `audio_scripts.py` file.
## Requirements
In order to run these functions you need to install the following packages:
* SciPy
* NumPy
* Matplotlib
* PySoundFile (provides an easier way to read wave files than scipy.io.wavfile.read used in the function `plot_wav` - no need to recalculate the amplitude range - therefore it's used for all the remainig functions)
