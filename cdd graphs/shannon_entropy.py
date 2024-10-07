import numpy as np
import matplotlib.pyplot as plt

# Crear un rango de valores para p en (0, 1) para evitar log(0)
p = np.linspace(0.01, 0.99, 400)  # Evitamos 0 y 1 exactos para evitar logaritmos indefinidos

# Calcular la entropía H(p)
H_p = p * np.log2(1 / p) + (1 - p) * np.log2(1 / (1 - p))

# Identificar el valor máximo en p=0.5
p_max = 0.5
H_max = p_max * np.log2(1 / p_max) + (1 - p_max) * np.log2(1 / (1 - p_max))

# Graficar
plt.figure(figsize=(8,6))
plt.plot(p, H_p, label=r'$H(p) = p \cdot \log_2\left(\frac{1}{p}\right) + (1-p) \cdot \log_2\left(\frac{1}{1-p}\right)$', color='blue')

# Agregar título y etiquetas
plt.title(r'Gráfico de $H(p)$ (solo valores positivos)')
plt.xlabel('p')
plt.ylabel('$H(p)$')

# Limitar los ejes para darle más altura al gráfico
plt.ylim(0, 1.2 * np.max(H_p))  # Aumentamos el límite superior del eje Y

# Marcar el punto máximo en p=0.5
plt.plot(p_max, H_max, 'ro')  # Un punto rojo en (0.5, H(0.5))
plt.axvline(x=p_max, color='red', linestyle='--', label=r'$p = 0.5$')  # Línea vertical en p=0.5

# Mostrar leyenda y cuadrícula
plt.legend()
plt.grid(True)

# Mostrar gráfico
plt.show()
