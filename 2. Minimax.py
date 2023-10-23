def mostrar_tablero(tablero):
    # Función para mostrar el tablero del juego
    print(tablero[0] + ' | ' + tablero[1] + ' | ' + tablero[2])
    print('---------')
    print(tablero[3] + ' | ' + tablero[4] + ' | ' + tablero[5])
    print('---------')
    print(tablero[6] + ' | ' + tablero[7] + ' | ' + tablero[8])

def minimax(tablero, jugador):
    # Función que implementa el algoritmo Minimax para determinar el valor de un estado del juego

    # Verificar si hay un ganador o empate en el estado actual del tablero
    ganador = verificar_ganador(tablero)
    if ganador == 'X':
        return -1
    elif ganador == 'O':
        return 1
    elif ganador == 'Empate':
        return 0

    # Maximizador (jugador 'O')
    if jugador == 'O':
        mejor_valor = -float("inf")
        for i in range(9):
            if tablero[i] == ' ':
                tablero[i] = jugador
                valor = minimax(tablero, 'X')
                tablero[i] = ' '
                mejor_valor = max(mejor_valor, valor)
        return mejor_valor

    # Minimizador (jugador 'X')
    else:
        mejor_valor = float("inf")
        for i in range(9):
            if tablero[i] == ' ':
                tablero[i] = jugador
                valor = minimax(tablero, 'O')
                tablero[i] = ' '
                mejor_valor = min(mejor_valor, valor)
        return mejor_valor

def movimiento_optimo(tablero):
    # Función que determina el movimiento óptimo para el jugador 'O' usando el algoritmo Minimax
    mejor_movimiento = -1
    mejor_valor = -float("inf")

    for i in range(9):
        if tablero[i] == ' ':
            tablero[i] = 'O'
            valor = minimax(tablero, 'X')
            tablero[i] = ' '
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_movimiento = i

    return mejor_movimiento

def verificar_ganador(tablero):
    # Función que verifica si hay un ganador o un empate en el tablero
    lineas_ganadoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    for linea in lineas_ganadoras:
        a, b, c = linea
        if tablero[a] == tablero[b] == tablero[c] and tablero[a] != ' ':
            return tablero[a]

    if ' ' not in tablero:
        return 'Empate'

    return None

# Ejemplo de uso
tablero = ['X', 'O', 'X', ' ', 'O', 'X', ' ', ' ', 'O']
mostrar_tablero(tablero)

ganador = verificar_ganador(tablero)
if ganador:
    print(f'Ganador: {ganador}')
else:
    mejor_movimiento = movimiento_optimo(tablero)
    tablero[mejor_movimiento] = 'O'
    mostrar_tablero(tablero)
