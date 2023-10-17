import random


p = ["algoritmo", "lenguaje", "compilador", "variable", "función", "ciclo", "bucle", "clase", "objeto", "herencia", "polimorfismo", "encapsulamiento", "modularidad", "depuración", "integración", "desarrollo", "frontend", "backend", "base de datos", "API", "framework", "librería", "programador", "sintaxis", "compilación", "interpretación", "enlace", "optimización", "repositorio", "código fuente"]


def choise(p):
    w = random.choice(p)
    return w


def show(secret, this):
    for sign in secret:
        if sign in this:
            print(sign, end=" ")
        else:
            print("_", end=" ")
    print()


def get_l(this):
    sign = input("Ingresa una letra: ")

    while len(sign) != 1 or not sign.isalpha():
        sign = input("Ingresa solo una letra: ")

    while sign in this:
        sign = input("Ya adivinaste esa letra, intenta otra: ")
    return sign


def horca():
    print("¡Bienvenido al juego del ahorcado!")
    secret = choise(p)
    this = []
    vida = 8

    while True:
        show(secret, this)
        sign = get_l(this)

        if sign in secret:
            this.append(sign)
            print("¡Muy bien! Adivinaste una letra.")
        else:
            vida -= 1
            print("Lo siento, esa letra no está en la palabra.")
            print("Te quedan", vida, "vidas.")

        if vida == 0:
            print("¡Perdiste! La palabra era:", secret)
            break
        elif set(secret) == set(this):
            print("¡Felicidades! Adivinaste la palabra:", secret)
            break


horca()
