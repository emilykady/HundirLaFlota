#inicialización y creación de matrices.
import random;

#tamaño del tablero
tamaño = 8
tableroVisible = []
tableroOculto = []

#tablero visible
for i in range(tamaño):
    fila = []
    for j in range(tamaño):
        fila.append("🌊")
    tableroVisible.append(fila)


#tablero no visible
for i in range(tamaño):
    fila = []
    for j in range(tamaño):
        fila.append("🌊")
    tableroOculto.append(fila)