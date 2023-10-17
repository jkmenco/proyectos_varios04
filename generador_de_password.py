import random

def password_generator(p):
    password = ''
    character = 'abcdefghijklmnopqrstuvwxyz1234567890'
    for i in range(p):
        password += random.choice(character)
    return password

password_length = int(input('¿Cuántos caracteres debe tener la contraseña? '))
print(f"Su contraseña es: {password_generator(password_length)}")
