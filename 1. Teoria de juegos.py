def juego_de_coordinacion(jugador1, jugador2):
    if jugador1 == "Cooperar" and jugador2 == "Cooperar":
        return "Ambos reciben una recompensa moderada"
    elif jugador1 == "Cooperar" and jugador2 == "Traicionar":
        return "Jugador 1 recibe una recompensa mínima, Jugador 2 recibe una recompensa máxima"
    elif jugador1 == "Traicionar" and jugador2 == "Cooperar":
        return "Jugador 1 recibe una recompensa máxima, Jugador 2 recibe una recompensa mínima"
    elif jugador1 == "Traicionar" and jugador2 == "Traicionar":
        return "Ambos reciben una recompensa moderada"
    else:
        return "Elecciones inválidas"

# Ejemplo de uso
jugador1 = "Cooperar"
jugador2 = "Traicionar"

resultado = juego_de_coordinacion(jugador1, jugador2)
print(resultado)
