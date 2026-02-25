import numpy as np
import matplotlib.pyplot as plt

# Tiempo
t = np.linspace(-5, 5, 1000)

# Función escalón
u = np.where(t >= 0, 1, 0)

# Gráfica
plt.plot(t, u)
plt.title("Función Escalón Unitario")
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.grid()
plt.show()
