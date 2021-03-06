# -*- coding: utf-8 -*-
"""preprocessing audio data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YQzKyh83Z_xhDrzg9XzR75LE-5WylBiJ
"""

import librosa,librosa.display
import matplotlib.pyplot as plt
import numpy as np

file = '/content/sample3.mp3'

signal, sr = librosa.load(file,sr=22000)
librosa.display.waveplot(signal,sr)
plt.xlabel("Time")
plt.ylabel("Amplitude")

"""# New Section"""

from google.colab import drive
drive.mount('/content/drive')

fft = np.fft.fft(signal)
magnitude=np.abs(fft)
frequency=np.linspace(0,sr,len(magnitude))
left_frequency=frequency[:int(len(frequency)/2)]
left_magnitude=magnitude[:int(len(frequency)/2)]
plt.plot(left_frequency,left_magnitude)
plt.xlabel("frequency")
plt.ylabel("magnitude")
plt.show()

#getting the spectrogram
n_fft=2048
hoplength=512
stft=librosa.core.stft(signal,n_fft=n_fft,hop_length=hoplength)
spectrogram=np.abs(stft)
log_spectrogram=librosa.amplitude_to_db(spectrogram)
librosa.display.specshow(log_spectrogram,sr=sr,hop_length=hoplength)
plt.xlabel("Time")
plt.ylabel("Magnitude")
plt.colorbar()
plt.show()

MFCC=librosa.feature.mfcc(signal,n_fft=n_fft,hop_length=hoplength,n_mfcc=13)
librosa.display.specshow(MFCC,sr=sr,hop_length=hoplength)
plt.xlabel("Time")
plt.ylabel("MFCC")
plt.colorbar()
plt.show()