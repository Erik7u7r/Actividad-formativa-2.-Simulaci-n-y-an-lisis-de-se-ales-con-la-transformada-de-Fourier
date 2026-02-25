Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... 
... # Parámetros
... fs = 1000
... t = np.linspace(-1, 1, fs, endpoint=False)
... 
... # Escalón manual
... u = np.where(t >= 0, 1, 0)
... 
... # FFT
... U = np.fft.fft(u)
... frecuencias = np.fft.fftfreq(len(u), 1/fs)
... 
... # Graficar frecuencias positivas
... plt.plot(frecuencias[:fs//2], np.abs(U)[:fs//2])
... plt.title("FFT - Función Escalón")
... plt.xlabel("Frecuencia (Hz)")
... plt.ylabel("Magnitud")
... plt.grid()
