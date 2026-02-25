Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... 
... # Parámetros
... A = 1
... f = 5            # frecuencia de la señal
... fs = 1000        # frecuencia de muestreo
... t = np.linspace(0, 1, fs, endpoint=False)
... 
... # Señal
... x = A * np.sin(2 * np.pi * f * t)
... 
... # Transformada de Fourier
... X = np.fft.fft(x)
... 
... # Frecuencias asociadas
... frecuencias = np.fft.fftfreq(len(x), 1/fs)
... 
... # Magnitud
... magnitud = np.abs(X)
... 
... # Graficar espectro
... plt.plot(frecuencias, magnitud)
... plt.title("Transformada de Fourier")
... plt.xlabel("Frecuencia (Hz)")
... plt.ylabel("Magnitud")
... plt.grid()
