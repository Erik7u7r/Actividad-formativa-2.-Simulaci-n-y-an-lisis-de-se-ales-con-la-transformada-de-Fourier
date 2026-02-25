import numpy as np
import matplotlib.pyplot as plt

# Crear eje de tiempo
t = np.linspace(-5, 5, 1000)

# Crear pulso rectangular
pulso = np.where((t >= -1) & (t <= 1), 1, 0)

# Graficar
plt.plot(t, pulso)
plt.title("Pulso Rectangular")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.grid()
plt.show()
