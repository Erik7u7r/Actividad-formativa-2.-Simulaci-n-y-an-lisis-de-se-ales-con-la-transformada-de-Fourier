Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... 
... # Parámetros
... fs = 1000
... t = np.linspace(-1, 1, fs, endpoint=False)
... 
... # Pulso rectangular manual
... pulso = np.where((t >= -0.2) & (t <= 0.2), 1, 0)
... 
... # FFT
... X = np.fft.fft(pulso)
... frecuencias = np.fft.fftfreq(len(pulso), 1/fs)
... 
... # Graficar solo frecuencias positivas
... plt.plot(frecuencias[:fs//2], np.abs(X)[:fs//2])
... plt.title("FFT - Pulso Rectangular")
... plt.xlabel("Frecuencia (Hz)")
... plt.ylabel("Magnitud")
... plt.grid()
