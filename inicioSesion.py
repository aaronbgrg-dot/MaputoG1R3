import json
import datetime
from os import system

# Formatear la fecha actual
fecha_hora = datetime.datetime.now()
FECHA = fecha_hora.strftime("%d/%m/%Y")
HORA = fecha_hora.strftime("%H:%M:%S")

with open("config.json", "r") as f:
    config = json.load(f)

def menu():
    global user, psw, FECHA, HORA
    system('cls')
    print(f'{FECHA:>208}')
    print(f'{HORA:>208}')
    print('')
    print(f'{'Introduzca usuario y contraseña:':^208}')
    print('')
    print('')
    user = str(input(f'{'Usuario: ':>106}'))
    psw = int(input(f'{'Contraseña: ':>107}'))

def user_error():
    global user, psw, FECHA, HORA
    system('cls')
    print(f'{FECHA:>208}')
    print(f'{HORA:>208}')
    print('')
    print(f'{'Error: Usuario no existe':^208}')
    print(f'{'Introduzca usuario y contraseña:':^208}')
    print('')
    print('')
    user = str(input(f'{'Usuario: ':>106}'))
    psw = int(input(f'{'Contraseña: ':>107}'))

def psw_error():
    global user, psw, FECHA, HORA
    system('cls')
    print(f'{FECHA:>208}')
    print(f'{HORA:>208}')
    print('')
    print(f'{'Error: Contraseña incorrecta':^208}')
    print(f'{'Introduzca usuario y contraseña:':^208}')
    print('')
    print('')
    user = str(input(f'{'Usuario: ':>106}'))
    psw = int(input(f'{'Contraseña: ':>107}'))

def correct_psw():
    global user, psw, FECHA, HORA
    system('cls')
    print(f'Usuario actual: {user.capitalize()}{FECHA:>188}')
    print(f'Puesto: {config['puesto'][user.lower()].capitalize()}{HORA:>195ñ}')
    print('')
    print(f'{'Introduzca usuario y contraseña:':^208}')
    print('')
    print('')
    print(f'{'Usuario: ' + f'{user}':>110}')
    print(f'{'Contraseña: ' + f'{psw}':>111}')
    print(f'{'Login correcto: Bienvenido/a ' + user.capitalize():^208}') 


menu()
while True:
    match user:
        case user if user not in config['users']:
            user_error()
        case user if psw != config['users'][f'{user.lower()}']:
            psw_error()
        case _:
            correct_psw()
            break