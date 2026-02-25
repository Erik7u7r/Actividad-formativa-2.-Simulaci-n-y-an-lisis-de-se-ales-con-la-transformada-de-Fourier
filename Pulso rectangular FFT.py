import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 1000
t = np.linspace(-1, 1, fs, endpoint=False)

# Pulso rectangular manual
pulso = np.where((t >= -0.2) & (t <= 0.2), 1, 0)

# FFT
X = np.fft.fft(pulso)
frecuencias = np.fft.fftfreq(len(pulso), 1/fs)

# Graficar solo frecuencias positivas
plt.plot(frecuencias[:fs//2], np.abs(X)[:fs//2])
plt.title("FFT - Pulso Rectangular")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()
plt.show()
