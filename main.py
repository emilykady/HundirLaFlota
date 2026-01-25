import game as game

seguir = True
print("------------Bienvenido a hundir la flota--------------\n")

while seguir:
    print("1- JUGADOR VS JUGADOR")
    print("2- JUGADOR VS MÁQUINA")
    print("3- MÁQUINA VS MÁQUINA")
    respuesta = input("Dime que modo vas a querer jugar: ")

    if respuesta == "1":
        game.jugadorVSjugador()
    elif respuesta == "2":
        game.jugadorMaquina()
    elif respuesta == "3":
        game.maquinaVSmaquina()

    print("\nVas a poder elegir otra vez el modo de juego")
    seguirJugando = input("Si quieres jugar otra vez responde (S), si no (N): ").upper()

    if seguirJugando == "N":
        seguir = False