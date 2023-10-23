import random

def funcion_evaluacion(intentos, numero_secreto, adivinanza):
    # Función de evaluación simple: devuelve la diferencia entre la adivinanza y el número secreto.
    return abs(adivinanza - numero_secreto)

def adivinar_numero(numero_secreto, rango_min, rango_max, intentos):
    print(f"Adivina el número secreto entre {rango_min} y {rango_max}.")

    for i in range(intentos):
        adivinanza = random.randint(rango_min, rango_max)
        print(f"Intento {i + 1}: {adivinanza}")

        diferencia = funcion_evaluacion(intentos, numero_secreto, adivinanza)

        if diferencia == 0:
            print(f"¡Felicidades! Adivinaste el número secreto ({numero_secreto}).")
            break
        else:
            if i == intentos - 1:
                print(f"¡Agotaste tus {intentos} intentos! El número secreto era {numero_secreto}.")
            else:
                print(f"Estás {'cerca' if diferencia <= 10 else 'lejos'}.")
                print("Intenta nuevamente.")

# Número secreto y rango
numero_secreto = random.randint(1, 100)
rango_min = 1
rango_max = 100

# Intentos permitidos
intentos = 5

# Juego
adivinar_numero(numero_secreto, rango_min, rango_max, intentos)
