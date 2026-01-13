"""
notas a futuro:
    · revisar si el funcionamiento es 100% correcto
    · intentar implementar con el resto del proyecto
"""

# Importar módulos
import json # <-- JSON para poder trabajar con archivos .json
import datetime # <-- para recoger los datos de la fecha/hora actual
import time # <-- para 'dormir' la ejecución del script en ciertos puntos 
from os import system # <-- para usar el comando 'cls' para limpiar pantalla
from random import randrange # <-- para crear una contraseña 'random'
from sys import exit # <-- para finalizar la ejecución del script de manera forzosa

# Formatear la fecha actual
fecha_hora = datetime.datetime.now()
FECHA = fecha_hora.strftime("%d/%m/%Y")
HORA = fecha_hora.strftime("%H:%M:%S")

# Contador de número de inicios de sesión incorrectos
num_error = 0

# Cargar datos de config.json
with open("config.json", "r") as f:
    config = json.load(f)

# Funcion menú login
def login_menu():
    global user, psw, num_error, FECHA, HORA
    # Limpia pantalla
    system('cls')
    # Imprime fecha/hora y varias líneas de texto
    print(f'{FECHA:>104}')
    print(f'{HORA:>104}')
    print('')
    print(f'{'Introduzca usuario y contraseña:':^104}')
    print('')
    print('')
    # Pide usuario y contraseña
    user = str(input(f'{'Usuario: ':>53}'))
    psw = int(input(f'{'Contraseña: ':>54}'))
    # Revisa usuario/contraseña
    match user:
        case user if user not in config['users']:
            login_error()
        case user if psw != config['users'][f'{user.lower()}']:
            login_error()
        case _:
            num_error = 0
            user_menu()

# Función para controlar usuario o contraseña incorrectos
def login_error():
    global num_error
    # Auementa el contador de errores
    num_error += 1
    # Si el recuento de errores alcanza 3 termina la ejecución del sript forzosamente
    if num_error == 3:
        print(f'{'Has alcanzado el límite de intentos, intentalo otra vez en otro momento.':^104}')
        time.sleep(2)
        exit()
    # Da un mensaje de error, enseña el número actual de errores y vuelve a la función login_menu() despues de esperar 2 segundos
    print(f'{'ERROR: Usuario o contraseña incorrectos':^104}')
    print(f'{'Llevas ' + str(num_error) + '/3 intentos.':^104}')
    time.sleep(2)
    login_menu()

# Menú de usuario
def user_menu():
    global FECHA, HORA, opcion
    # Limpia la pantalla e imprime la siguiente información en las esquinas de la pantalla:
    # Usuario actual, puesto del usuario, fecha actual, y hora actual
    system('cls')
    print(f'Usuario actual: {user.capitalize()}{FECHA:>94}')
    print(f'Puesto: {config['puesto'][user.lower()].capitalize()}{HORA:>101}')
    print('')
    print('')
    # Imprime las diferentes opciones que puede tomar el usuario
    print(f'{'Bienvenido/a ' + str(user.capitalize()):^104}')
    print(f'{'¿Que desea hacer?':^104}')
    print('')
    print(f'{'1. Ir al menú principal':^104}')
    print(f'{'2. Generar contraseña nueva':^104}')
    print(f'{'3. Cerrar Sesión':^104}')
    print('')
    # Pide la opción y salta a la función user_option() para ejecutar la opción
    opcion = int(input(f'{'>'*3:>51} '))
    user_option()

# Función que controla las opciones de user_menu()
def user_option():
    global opcion
    while True:
        # Dependiendo el valor de la variable opcion hace lo siguiente:
        match opcion:
            case 1:
                #Actualmente no hace nada
                #Añadir menu desarrollado por Xabier
                pass
            case 2:
                # Genera una contraseña nueva entre los posibles valores 0000 y 9999
                new_psw = randrange(0000, 9999, 1)
                # Guarda la nueva contraseña y sobreescribe el archivo config.json para guardar la nueva contraseña entre ejecuciones
                config['users'][user.lower()] = new_psw
                with open('config.json', 'w') as f:
                    json.dump(config, f)
                # Muestra la nueva contraseña al usuario y vuelve al menu principal en user_menu()
                print(f'{'Contraseña cambiada a: ' + str(new_psw):^104}')
                input(f'{'Pulse culaquier tecla para continuar:':^104}')
                user_menu()
            case 3:
                # Da un mensaje de despedida y termina la ejecución del script forzosamente
                print('')
                print(f'{'Gracias por usar el programa, vuelva pronto :)':^104}')
                exit()
            case _:
                # Si el usuario introduce un valor incorrecto da un mensaje de error y pide un nuevo valor
                print(f'{'ERROR: Introduce una opción válida':^104}')
                opcion = input(f'{'>'*3:>51} ')

login_menu()