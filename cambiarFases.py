import sqlite3 as sql 
BASE = 'Maputo_SL.db'
import random

def insertarMontaje():
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    coche = int(input("Que coche quieres introducir en esta fase?"))
    horas = input("Cuantas horas va a estar?")
    numRandom = random.random()
    if numRandom < 0.10 :
        error = input("Ha saltado un error. Cual ha sido el motivo? ")
        cursor.execute(f"""INSERT INTO error (Id_Coche, Contador, Motivo) VALUES ({coche}, 1, "{error}")""")
    
    cursor.execute(f"""INSERT INTO montaje (Id_Coche, Horas, PrecioHora, Status) VALUES ({coche},{horas},30,'Activo')""")
    conn.commit()
    conn.close()

def insertarPintado():
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    coche = int(input("Que coche quieres introducir en esta fase?"))
    horas = input("Cuantas horas va a estar?")
    numRandom = random.random()
    if numRandom < 0.10 :
        error = input("Ha saltado un error. Cual ha sido el motivo? ")
        cursor.execute(f"""INSERT INTO error (Id_Coche, Contador, Motivo) VALUES ({coche}, 1, "{error}")""")
    
    cursor.execute(f"""INSERT INTO pintado (Id_Coche, Horas, PrecioHora, Status) VALUES ({coche},{horas},20,'Activo')""")
    conn.commit()
    conn.close()

def insertarAcabado():
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    coche = int(input("Que coche quieres introducir en esta fase?"))
    horas = input("Cuantas horas va a estar?")
    numRandom = random.random()
    if numRandom < 0.10 :
        error = input("Ha saltado un error. Cual ha sido el motivo? ")
        cursor.execute(f"""INSERT INTO error (Id_Coche, Contador, Motivo) VALUES ({coche}, 1, "{error}")""")
    
    cursor.execute(f"""INSERT INTO acabado (Id_Coche, Horas, PrecioHora, Status) VALUES ({coche},{horas},10,'Activo')""")
    conn.commit()
    conn.close()






def selectCoches():
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM coches')
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)


if __name__ == "__main__":
    selectCoches()