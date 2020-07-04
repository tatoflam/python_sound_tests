import numpy as np
from scipy.io import wavfile
import scipy.signal

frequency = 440.0
seconds = 1.0
rate = 44100

phases = np.cumsum(2.0 * np.pi * frequency / rate * np.ones(int(rate * seconds)))

wave = np.sin(phases)
wave_sawtooth = scipy.signal.sawtooth(phases)
wave_square = scipy.signal.square(phases)


# write 16 bit wav file
wave = (wave * float(2 **15 -1)).astype(np.int16)
wavfile.write("sin.wav", rate, wave)


wave_sawtooth = (wave_sawtooth * float(2 **15 -1)).astype(np.int16)
wave_square = (wave_square * float(2 **15 -1)).astype(np.int16)

wavfile.write("sawtooth.wav", rate, wave_sawtooth)
wavfile.write("square.wav", rate, wave_square)



