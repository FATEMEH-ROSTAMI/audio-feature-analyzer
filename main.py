import numpy as np
import librosa
import matplotlib.pyplot as plt

audio,sr=librosa.load("test1.wav",sr=None,mono=True)
duration=len(audio)/sr
rms=np.sqrt(np.mean(audio**2))

print("sample rate:",sr)
print("number of sample:",len(audio))
print("duration:",duration,"seconds")
print("RMS:",rms)

time=np.arange(len(audio))/sr

plt.figure(figsize=(12,4))
plt.plot(time,audio)

plt.xlabel("time(second)")
plt.ylabel("amplitude")
plt.title("test1")
plt.grid()
plt.show()
