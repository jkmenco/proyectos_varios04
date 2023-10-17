def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

print("¡Bienvenido a la calculadora básica!")
print("Seleccione la operación que desea realizar.")

print("Operaciones disponibles:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = input("Ingrese el número de la operación que desea realizar: ")

print("Ingrese dos números para realizar su operación")


num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")



if opcion == 1:
    resultado = sumar(num1, num2)
elif opcion == 2:
    resultado = restar(num1, num2)
elif opcion == 3:
    resultado = multiplicar(num1, num2)
elif opcion == 4:
    resultado = dividir(num1, num2)
else:
    print("Opción inválida")

print("El resultado de la operación es: ", resultado)
