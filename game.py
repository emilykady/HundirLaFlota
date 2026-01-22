#inicialización y creación de matrices.
import random;

#TABLERO
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


#BARCOS
barcos = 3
barcosEnMapa = 0

while barcos < barcosEnMapa:
    filas = random.randint(0, tamaño-1)
    columnas = random.randint(0, tamaño-1)

    #si la casilla esta vacia (es agua) ponemos barco
    if tableroOculto[filas][columnas] == "🌊":
        tableroOculto[filas][columnas] = "🚢"
        barcosEnMapa += 1
    

barcosHundidos = 0
disparos = 0

while barcosHundidos < barcos:
    print("0  1  2  3  4")

    for i in range(tamaño):
        fila_texto = " ".join(tableroVisible[i])
        print(f"{i} {fila_texto}")

        try:
            filas = int(input("\nFila (0-{TAMANO-1}):"))
            columnas = int(input("\nColumna (0-{TAMANO-1}):"))

            if(filas < 0 or filas >= tamaño or columnas < 0 or columnas >= tamaño):
                print("Esa coordenada no existe")
                continue
            if tableroVisible[filas][columnas] != "🌊":
                print("Ya disparaste ahí.")
                continue
        except ValueError:
            print("Por favor, escribe un número.")
        continue
