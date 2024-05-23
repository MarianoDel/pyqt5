from scipy.io.wavfile import write
import numpy as np

samplerate = 44100;
fs1 = 500
fs2 = 800
t = np.linspace(0., 1., samplerate)
amplitude = np.iinfo(np.int16).max
first = amplitude * np.sin(2. * np.pi * fs1 * t)
second = amplitude * np.sin(2. * np.pi * fs2 * t)
first_cut = first[:int(len(first) / 10)]
first_cut = first_cut.astype(np.int16)
second_cut = second[:int(len(second) / 10)]
second_cut = second_cut.astype(np.int16)

zeros_len = first[:int(len(first) / 2)]
zeros = np.zeros_like(zeros_len)

data = np.concatenate((first_cut, second_cut))
data = np.concatenate((zeros, data))
write("up_long3.wav", samplerate, data.astype(np.int16))

data = np.concatenate((second_cut, first_cut))
data = np.concatenate((zeros, data))
write("down_long3.wav", samplerate, data.astype(np.int16))
