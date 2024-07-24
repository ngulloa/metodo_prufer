from progress.bar import ChargingBar
import matplotlib.pyplot as plt
import numpy as np

n_valor_propio = int(input("N-ésimo valor propio a calcular: "))
n = int(input("Cantidad de puntos para muestreo (suficientemente grande): "))

l=1
xa = 0
xb = 1
he = 0.1
hx = (xb-xa)/n 

# Aquí se define el potencial
def potencial(x):
    return 0

# Lista que contendrá los puntos de E
E = []

# Lista que contendrá los puntos de T
T = []

# Contadores
n_actual = 0
i=0

#Barra de progreso
bar = ChargingBar("Procesando", max = n_valor_propio)

while n_actual<n_valor_propio:
    
    # Secuencias iniciales
    p = [1,1]
    thetha = [0]
    
    for k in range(0, n-2):
        pk2 = ((l**2/p[k]**3) + potencial(k*hx)*p[k] - i*p[k])*(hx**2) + 2*p[k+1] - p[k]
        p.append(pk2)

        thetha1 = (l*hx)/(p[k]**2) + thetha[k]
        thetha.append(thetha1)
    
    i += he
    
    # Último valor de la secuencia thetha
    thetha1 = (l*hx)/(p[(n-2)]**2) + thetha[n-2]
    thetha.append(thetha1)

    # Construcción de secuencia E y T
    E.append(i)
    T.append(thetha[-1]/np.pi)

    # Condición de término
    if int(T[-1]) > n_actual:
        n_actual = int(T[-1])
        bar.next()
        
# Final barra de progreso
bar.finish()

# Output en consola
print(f"Valor de energía con n = {round(T[-1])} es {E[-1]}")

# Crear la gráfica
plt.plot(E, T)
plt.grid(True)

# Añadir títulos y etiquetas
plt.title('Gráfica de T(E)')
plt.xlabel('E')
plt.ylabel('T')

# Mostrar la gráfica
plt.show()