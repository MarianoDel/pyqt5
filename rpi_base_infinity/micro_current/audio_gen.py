from scipy.io.wavfile import write
import numpy as np

samplerate = 44100;
fs1 = 500
fs2 = 800
t = np.linspace(0., 1., samplerate)
amplitude = np.iinfo(np.int16).max
first = amplitude * np.sin(2. * np.pi * fs1 * t)
second = amplitude * np.sin(2. * np.pi * fs2 * t)
first = first[:int(len(first) / 10)]
first = first.astype(np.int16)
second = second[:int(len(second) / 10)]
second = second.astype(np.int16)
data = np.concatenate((first, second))
write("up.wav", samplerate, data.astype(np.int16))

data = np.concatenate((second, first))
write("down.wav", samplerate, data.astype(np.int16))
