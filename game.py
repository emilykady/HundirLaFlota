import random
import time

#basico
def crearTablero(tamaño):
    tablero = []
    for i in range(tamaño):
        fila = []
        for j in range(tamaño):
            fila.append("🌊")
        tablero.append(fila)
    return tablero

def imprimirTablero(tablero, tamaño, nombre):
    print(f"Tablero de {nombre}")
    print("0 1 2 3 4 5 6 7")
    for i in range(tamaño):
        fila_texto = " ".join(tablero[i])
        print(f"{i}  {fila_texto}")

def colocarBarcos(tablero, cantidad, tamaño):
    barcosEnMapa = 0

    while barcosEnMapa < cantidad:
        filas = random.randint(0, tamaño-1)
        columnas = random.randint(0, tamaño-1)
        if tablero[filas][columnas] == "🌊":
            tablero[filas][columnas] = "🚢"
            barcosEnMapa += 1

#TURNOS

def disparos(filas, columnas, tableroOculto, tableroVisible):
    if tableroOculto[filas][columnas] == "🚢":
        print("TOCADO Y HUNDIDO")
        tableroVisible[filas][columnas] = "🔥"
        return True
    else:
        print("💧 Agua...")
        tableroVisible[filas][columnas] = "💧"
        return False

def turnoJugador(tableroOculto, tableroVisible, tamaño, nombre):
    while True:
        while True:
            try:
                print(f"\nTurno de {nombre}")
                filas = int(input(f"Fila (0-{tamaño-1}): "))
                columnas = int(input(f"Columna (0-{tamaño-1}): "))
                
                if filas < 0 or filas >= tamaño or columnas < 0 or columnas >= tamaño:
                    print("Coordenada fuera de rango.")
                    continue
                if tableroVisible[filas][columnas] != "🌊":
                    print("Ya disparaste ahí.")
                    continue
                
                return disparos(filas, columnas, tableroOculto, tableroVisible)
            except ValueError:
                print("Error: Escribe números enteros.")


def turnoMaquina(tableroOCulto, tableroVisible, tamaño):

    while True:
        filas = random.randint(0, tamaño - 1)
        columnas = random.randint(0, tamaño - 1)
        if tableroVisible[filas][columnas] == "🌊":
            print(f"\nLa Máquina dispara a ({f}, {c})...")
            time.sleep(1) 
            # return disparos(filas, columnas, tableroOculto, tableroVisible)
        

# MODOS DE JUEGO 
