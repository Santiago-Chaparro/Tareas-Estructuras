# Tablero como lista 1D (9 casillas)
tablero = [" "]*9

# Combinaciones ganadoras
ganar = [
    [0,1,2], [3,4,5], [6,7,8],  # filas
    [0,3,6], [1,4,7], [2,5,8],  # columnas
    [0,4,8], [2,4,6]            # diagonales
]

jugador = "X"

for turn in range(9):
    # Mostrar tablero como lista
    print(tablero[0:3])
    print(tablero[3:6])
    print(tablero[6:9])

    # Jugada
    casilla = int(input(f"\nTurno de {jugador}, elige casilla (0-8): "))

    if tablero[casilla] == " ":
        tablero[casilla] = jugador
    else:
        print("Casilla ocupada, intenta otra vez.")
        continue

    # Verificar ganador
    if any(all(tablero[i] == jugador for i in combo) for combo in ganar):
        print(tablero[0:3])
        print(tablero[3:6])
        print(tablero[6:9])
        print(f"\nJugador {jugador} gana")
        break

    # Cambiar jugador
    jugador = "O" if jugador == "X" else "X"
else:
    print(tablero[0:3])
    print(tablero[3:6])
    print(tablero[6:9])
    print("\nEmpate")
