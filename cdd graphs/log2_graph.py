import numpy as np
import matplotlib.pyplot as plt

# Crear un rango de valores para x menores a 1 para que log2(1/x) sea positivo
x = np.linspace(0.1, 0.99, 400)  # Rango de 0.1 a 0.99 para asegurar I(x) > 0

# Calcular logaritmo base 2 de 1/x, que es equivalente a -log2(x)
y = -np.log2(x)

# Graficar
plt.figure(figsize=(8,6))
plt.plot(x, y, label=r'$I(p) = \log_2\left(\frac{1}{p}\right)$', color='blue')

# Agregar título y etiquetas
plt.title(r'Gráfico de $I(p) = \log_2\left(\frac{1}{p}\right)$')
plt.xlabel('p')
plt.ylabel('$I(p)$')

# Limitar los ejes para mostrar solo valores positivos de I(x)
plt.ylim(0, np.max(y))

# Mostrar cuadrícula y leyenda
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()

