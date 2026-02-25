import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 1000
t = np.linspace(-1, 1, fs, endpoint=False)

# Escalón manual
u = np.where(t >= 0, 1, 0)

# FFT
U = np.fft.fft(u)
frecuencias = np.fft.fftfreq(len(u), 1/fs)

# Graficar frecuencias positivas
plt.plot(frecuencias[:fs//2], np.abs(U)[:fs//2])
plt.title("FFT - Función Escalón")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud")
plt.grid()
plt.show()
