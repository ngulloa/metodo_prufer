"""Módulo para resolver la ecuación de Schrödinger simplificada utilizando el método de Shooting y graficar la solución"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros
n = 2000
xa = 0
xb = 1
h = (xb - xa) / n
tolerancia = 0.0001
u0 = 0     # primera condición inicial (u)
du0 = 1    # segunda condición inicial (du/dx)

# Definición del potencial
def potencial(x):
    return 0

# Obtener función objetivo
def funcion_objetivo(E):
    u = [u0, du0 * h + u0] 
    # Integrar discretamente hacia delante
    for i in range(0, n-1):
        u2 = 2 * u[i+1] - u[i] + (h ** 2) * (potencial(xa + i*h) - E) * u[i+1]
        u.append(u2)
    return u[-1] # Retornar último valor

# Obtener derivada de función objetivo
def derivar(funcion,x , h: int):
    # se utiliza diferencias finitas
    derivada = (funcion_objetivo(x + h) - funcion_objetivo(x))/h
    return derivada



# Método de Newton-Rhapson

# Primera aproximación
x_aprox = float(input("Primera aproximación: "))
k = round(x_aprox)+1 # máximo valor en el dominio E

# Obtención de función objetivo
dominio = np.linspace(0, k, n)
f = [funcion_objetivo(E) for E in dominio]

# Ajustar aproximación
m = funcion_objetivo(x_aprox)/derivar(funcion_objetivo,x_aprox,h) 

while True:
    if np.abs(funcion_objetivo(x_aprox))<tolerancia:
        break
    m = funcion_objetivo(x_aprox)/derivar(funcion_objetivo,x_aprox,h)
    x_aprox -= m

print("E = ", x_aprox)

#Graficar f(E)
plt.plot(dominio, f)
plt.axhline(0, color='red', linestyle='--')
plt.grid(True)
plt.title('Función Objetivo')
plt.xlabel('E')
plt.ylabel('f(E)')
plt.show()