Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... 
... # Parámetros
... A = 2          # Amplitud
... f = 5          # Frecuencia en Hz
... phi = 0        # Fase
... t = np.linspace(0, 1, 1000)
... 
... # Señal senoidal
... x = A * np.sin(2 * np.pi * f * t + phi)
... 
... # Gráfica
... plt.plot(t, x)
... plt.title("Función Senoidal")
... plt.xlabel("Tiempo")
... plt.ylabel("Amplitud")
... plt.grid()
