import sqlite3 as sql 
BASE = 'Maputo_SL.db'
import random

def insertarMontaje():
    # Se conecta a la base de datos
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    # Pide los datos que se van a introducir a la tabla 'montaje'
    coche = int(input("Que coche quieres introducir en esta fase? >> "))
    horas = input("Cuantas horas va a estar? >> ")
    # Genera un número aleatorio y si se cumple la condicion muestra un mensaje de error
    numRandom = random.random()
    if numRandom < 0.10 :
        error = input("Ha saltado un error. Cual ha sido el motivo? >> ")
        cursor.execute(f"""INSERT INTO error (Id_Coche, Contador, Motivo) VALUES ({coche}, 1, "{error}")""")
    # Inserta los valores de las variables 'coche' y 'horas' a la tabla "montaje" de la base de datos
    cursor.execute(f"""INSERT INTO montaje (Id_Coche, Horas, PrecioHora, Status) VALUES ({coche},{horas},30,'Activo')""")
    conn.commit()
    conn.close()

def insertarPintado():
    # Se conecta a la base de datos
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    # Pide los datos que se van a introducir a la tabla "pintado"
    coche = int(input("Que coche quieres introducir en esta fase? >> "))
    horas = input("Cuantas horas va a estar? >> ")
    # Genera un número aleatorio y si se cumple la condicion muestra un mensaje de error
    numRandom = random.random()
    if numRandom < 0.10 :
        error = input("Ha saltado un error. Cual ha sido el motivo? >> ")
        cursor.execute(f"""INSERT INTO error (Id_Coche, Contador, Motivo) VALUES ({coche}, 1, "{error}")""")
    # Inserta los valores de las variables 'coche' y 'horas' a la tabla "pintado" de la base de datos
    cursor.execute(f"""INSERT INTO pintado (Id_Coche, Horas, PrecioHora, Status) VALUES ({coche},{horas},20,'Activo')""")
    conn.commit()
    conn.close()

def insertarAcabado():
    # Se conecta a la base de datos
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    # Pide los datos que se van a introducir a la tabla "acabado"
    coche = int(input("Que coche quieres introducir en esta fase? >> "))
    horas = input("Cuantas horas va a estar? >> ")
    # Genera un número aleatorio y si se cumple la condicion muestra un mensaje de error
    numRandom = random.random()
    if numRandom < 0.10 :
        error = input("Ha saltado un error. Cual ha sido el motivo? >> ")
        cursor.execute(f"""INSERT INTO error (Id_Coche, Contador, Motivo) VALUES ({coche}, 1, "{error}")""")
    # Inserta los valores de las variables 'coche' y 'horas' a la tabla "acabado" de la base de datos
    cursor.execute(f"""INSERT INTO acabado (Id_Coche, Horas, PrecioHora, Status) VALUES ({coche},{horas},10,'Activo')""")
    conn.commit()
    conn.close()

def selectCoches():
    # Se conecta a la base de datos
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    # Selecciona todos los elementos de la tabla coches
    cursor.execute('SELECT * FROM coches')
    # Imprime los valores seleccionados de la tabla coches
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

if __name__ == "__main__":
    selectCoches()