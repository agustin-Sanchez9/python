import numpy as np
import matplotlib.pyplot as plt

Fs = 500
T = 1/Fs
L = 1000
t = np.linspace(0,L*T,L,endpoint=False)

f1 = 100
f2 = 50 
f3 = 75

signal = np.cos(2*np.pi*f1*t) + 0.75*np.sin(2*np.pi*f2*t) + 2*np.cos(2*np.pi*f3*t)

signal_fft = np.fft.fft(signal)
freq = np.fft.fftfreq(L,T)

signal_fft_abs = np.abs(signal_fft)

plt.subplot(2, 1, 1)
plt.plot(t, signal)

plt.subplot(2,1,2)
plt.plot(freq,signal_fft_abs)

plt.show()