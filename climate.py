import random

# Definimos una lista con los diferentes estados del clima
estados_clima = ["soleado", "lluvioso", "nublado"]

# Creamos una función para generar el clima aleatorio
def generar_clima():
    clima = random.choice(estados_clima)
    return clima

# Pedimos al usuario que introduzca el número de días para simular el clima
dias_simulados = int(input("¿Cuántos días quieres simular el clima? "))

# Simulamos el clima para el número de días especificado
for i in range(dias_simulados):
    clima_dia = generar_clima()
    print("El clima para el día", i+1, "es:", clima_dia)
