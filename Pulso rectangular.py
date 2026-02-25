Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import numpy as np
... import matplotlib.pyplot as plt
... 
... # Crear eje de tiempo
... t = np.linspace(-5, 5, 1000)
... 
... # Crear pulso rectangular
... pulso = np.where((t >= -1) & (t <= 1), 1, 0)
... 
... # Graficar
... plt.plot(t, pulso)
... plt.title("Pulso Rectangular")
... plt.xlabel("Tiempo")
... plt.ylabel("Amplitud")
... plt.grid()
