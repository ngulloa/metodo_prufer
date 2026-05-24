# Resumen 📄

Este proyecto tiene como objeto ser una guía útil y un **apoyo pedagógico** para la **aplicación de métodos numéricos en mecánica cuántica**. En concreto, se estudia la aplicación de dos métodos (y algunos sub-métodos) que permiten encontrar los valores de energía para distintos estados de la función de onda con algún potencial conocido.

En particular, se estudia el método de _las variables de Prüfer_ y el método de _Shooting_ (o _disparo_, en español).

## Contenido del repositorio
En este repositorio encontrarás:
 - El archivo ```metodo_de_prufer.pdf```, contiene los lineamientos teóricos y prácticos para la comprensión del método de Prüfer.
 - El archivo ```prufer.py```, contiene el código escrito en python que ejecuta el método de Prüfer.
 - El archivo ```metodo_de_Shooting.pdf```, contiene los lineamientos teóricos y prácticos para la comprensión del método de Shooting.
 - El archivo ```shooting.py```, contiene el código escrito en python que ejecuta el método de Shooting.

## Alcances y limitaciones
A continuación se listan los alcances y limitaciones de cada archivo ```.py```: 
### ```prufer.py ```
 
 - ✅ Permite encontrar el enésimo valor propio (energía) para alguna función de onda definida en un dntervalo finito, con algún potencial dado (ver SECCION).
 - ✅ Permite gestionar la cantidad de puntos con las que se realizan las aproximaciones numéricas.
 - ✅ Se obtiene una representación gráfica del mapa $T$ en función de $E \in \mathcal{N}$ (ver ```metodo_de_prufer.pdf```).
 - ❌ Para estados muy altos y/o mucha cantidad de puntos la ejecución del código puede tomar demasiado tiempo.
 - ❌ La correcta ejecución se limita solo a funciones de onda definidas en intervalos finitos.

### ```shooting.py ```
 
 - ✅ Permite encontrar el valor propio (energía) más cercano a alguna aproximación inicial (ver SECCION).
 - ✅ Se obtiene una representación gráfica de la función objetivo versus la energía (ver ```metodo_de_Shooting.pdf```).
 - ✅ Se ejecuta rápidamente, por lo que es útil para encontrar elevados valores de energía.
 - ❌ La correcta ejecución se limita solo a funciones de onda definidas en intervalos finitos.


# REQUISITOS E INSTALACION 💻
## Requisitos Previos

Asegúrate de tener instalados **Python 3.7** o superior y las siguientes librerias:
 - progress
 - matpltlib
 - numpy



