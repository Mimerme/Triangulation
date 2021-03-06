import pyaudio
import numpy as np
import pdb
import matplotlib.pyplot as plt

p = pyaudio.PyAudio()

volume = 0.005     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 15.0   # in seconds, may be float
f = 50        # sine frequency, Hz, may be float

#Hidden audio is within the audible frequency range
hidden = np.cos((2*np.pi*np.arange(fs*duration)*50)/fs).astype(np.float32)
carrier = np.cos((2*np.pi*np.arange(fs*duration)*10)/fs).astype(np.float32)

x = (2*np.pi*np.arange(fs*duration)*50)/fs
plt.plot(x[:10000], hidden[:10000])
plt.show()

plt.plot(x[:10000], carrier[:10000])
plt.show()

sin = ((hidden * carrier) + carrier).astype(np.float32)
# generate samples, note conversion to float32 array
samples = sin + (sin * sin)

plt.plot(x[:10000], samples[:10000])
plt.show()
#samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)


# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively) 
stream.write(volume*samples)

stream.stop_stream()
stream.close()

p.terminate()