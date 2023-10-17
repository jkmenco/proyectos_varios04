import random

# Lista de palabras para elegir
palabras = ["python", "programacion", "ordenador", "juego", "hacker", "tecnologia", "desarrollo"]

# Función para elegir una palabra al azar
def elegir_palabra(palabras):
    palabra = random.choice(palabras)
    return palabra

# Función para mostrar el progreso del juego
def mostrar_progreso(palabra_oculta, letras_adivinadas):
    for letra in palabra_oculta:
        if letra in letras_adivinadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()

# Función para pedir al usuario una letra
def pedir_letra(letras_adivinadas):
    letra = input("Ingresa una letra: ")
    # Validar que solo se ingrese una letra
    while len(letra) != 1 or not letra.isalpha():
        letra = input("Ingresa solo una letra: ")
    # Validar que no se haya adivinado la letra antes
    while letra in letras_adivinadas:
        letra = input("Ya adivinaste esa letra, intenta otra: ")
    return letra

# Función para jugar al ahorcado
def jugar_ahorcado():
    print("¡Bienvenido al juego del ahorcado!")
    palabra_oculta = elegir_palabra(palabras)
    letras_adivinadas = []
    vidas = 6

    while True:
        mostrar_progreso(palabra_oculta, letras_adivinadas)
        letra = pedir_letra(letras_adivinadas)

        if letra in palabra_oculta:
            letras_adivinadas.append(letra)
            print("¡Muy bien! Adivinaste una letra.")
        else:
            vidas -= 1
            print("Lo siento, esa letra no está en la palabra.")
            print("Te quedan", vidas, "vidas.")

        if vidas == 0:
            print("¡Perdiste! La palabra era:", palabra_oculta)
            break
        elif set(palabra_oculta) == set(letras_adivinadas):
            print("¡Felicidades! Adivinaste la palabra:", palabra_oculta)
            break

# Iniciar el juego
jugar_ahorcado()
