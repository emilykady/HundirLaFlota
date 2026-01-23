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
        tableroVisible[filas][columnas] = "💀"
        return True
    else:
        print("💧 Agua...")
        tableroVisible[filas][columnas] = "🌫️"
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


def turnoMaquina(tableroOculto, tableroVisible, tamaño):

    while True:
  
        filas = random.randint(0, tamaño - 1)
        columnas = random.randint(0, tamaño - 1)

        if tableroVisible[filas][columnas] == "🌊":
            print(f"\nLa Máquina dispara a ({filas}, {columnas})...")
            time.sleep(1) 
            return disparos(filas, columnas, tableroOculto, tableroVisible) 
        

# MODOS DE JUEGO 

#1 JUGADOR - MAQUINA
def jugadorMaquina():
    tamaño = 8
    barcos = 3

    tableroVisibleMaquina = crearTablero(tamaño)
    tableroOcultoMaquina = crearTablero(tamaño)
    colocarBarcos(tableroOcultoMaquina, barcos, tamaño)

    tableroVisibleJugador = crearTablero(tamaño)
    tableroOcultoJugador = crearTablero(tamaño)
    colocarBarcos(tableroOcultoJugador, barcos, tamaño)

    hundidosMaquina = 0
    hundidosJugador = 0
    disparos = 0

    while hundidosJugador < barcos and hundidosMaquina < barcos:
        imprimirTablero(tableroVisibleMaquina, tamaño, "Maquina")
        
        if turnoJugador(tableroOcultoMaquina, tableroVisibleMaquina, tamaño, "User"):
            hundidosMaquina += 1
        disparos += 1
        if hundidosMaquina == barcos:
            break

        if turnoMaquina(tableroOcultoJugador, tableroVisibleJugador, tamaño):
            hundidos_jugador += 1
    
        if hundidosMaquina == barcos:
            print(f"\n ¡GANASTE! Usaste {disparos} disparos.") 
        else:
            print("\nLA MÁQUINA HA GANADO...")


# 2 JUGADOR - JUGADOR.
def jugadorVSjugador():

    tamaño = 8
    barcos = 3

    tableroVisibleJugador1 = crearTablero(tamaño)
    tableroOcultoJugador1 = crearTablero(tamaño)
    colocarBarcos(tableroOcultoJugador2, barcos, tamaño)

    tableroVisibleJugador2 = crearTablero(tamaño)
    tableroOcultoJugador2 = crearTablero(tamaño)
    colocarBarcos(tableroOcultoJugador1, barcos, tamaño)

    hundidosJugador2 = 0
    hundidosJugador1 = 0
    disparos = 0

    while hundidosJugador1 < barcos and hundidosJugador2 < barcos:
        imprimirTablero(tableroOcultoJugador1, tamaño, "Maquina")
        
        if turnoJugador(tableroOcultoJugador2, tableroVisibleJugador2, tamaño, "Jugador 1"):
            hundidosJugador2 += 1
        disparos += 1
        if hundidosJugador2 == barcos:
            break

        if turnoJugador(tableroOcultoJugador1, tableroVisibleJugador1, tamaño, "Jugador 2"):
            hundidos_jugador += 1
    
        if hundidos_jugador == barcos:
            print(f"\n ¡GANASTE! Jugador 1 Usaste {disparos} disparos.") 
        else:
            print(f"\n ¡GANASTE! Jugador 2 Usaste {disparos} disparos.")


def maquinaVSmaquina():
    tamaño = 8
    barcos = 3

    tableroVisibleJugador1= crearTablero(tamaño)
    tableroOcultoJugador1 = crearTablero(tamaño)
    colocarBarcos(tableroOcultoJugador1, barcos, tamaño)

    tableroVisibleJugador2 = crearTablero(tamaño)
    tableroOcultoJugador2 = crearTablero(tamaño)
    colocarBarcos(tableroOcultoJugador2, barcos, tamaño)

    hundidosJugador1 = 0
    hundidosJugador2 = 0
    disparos = 0

    while hundidosJugador1 < barcos and hundidosJugador2 < barcos:
        imprimirTablero(tableroVisibleJugador1, tamaño, "Maquina")
        
        if turnoMaquina(tableroOcultoJugador1, tableroVisibleJugador1, tamaño):
            hundidosJugador1 += 1
        disparos += 1
        if hundidosJugador1 == barcos:
            break

        if turnoMaquina(tableroOcultoJugador2, tableroVisibleJugador2, tamaño):
            hundidosJugador2 += 1
    
        if hundidosJugador2 == barcos:
            print(f"\n ¡GANÓ LA MAQUINA 2! Usaste {disparos} disparos.") 
        else:
            print(f"\n ¡GANÓ LA MAQUINA 1! Usaste {disparos} disparos.")