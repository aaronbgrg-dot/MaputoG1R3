import sqlite3 as sql

#constante con el str del nombre de la base de datos
BASE = 'Maputo_SL.db'

def solicitarErrores():
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    coche = int(input("De que coche quieres sacar los errores? >> "))
    if coche < 6 and coche >0 :
        cursor.execute(f"SELECT Id_Error as Error, Id_Coche as Coche, Motivo FROM error WHERE Id_Coche = {coche}")
        fila = cursor.fetchall()
        print(f"\n{"Id_Error":^10}{"Id_Coche":^10}{"Motivo":^50}")
        print("_" * 70)
        for f in fila:
            print(f"{f[0]:^10}{f[1]:^10}{f[2]:^50}")
    else: 
        print("NO HAS SELECCIONADO UN COCHE DISPONIBLE")
    cursor.fetchall()
    conn.commit() 
    conn.close

def contadorErroes():
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    coche = int(input("De que coche quieres sacar los errores? >> "))
    if coche < 6 and coche >0 :
        cursor.execute(f"SELECT Id_Coche as Coche, SUM(Contador) as contador FROM error WHERE Id_Coche = {coche}")
        fila = cursor.fetchall()
        print(f"\n{"Coche":^10} {"Contador":^10}")
        print("_" * 21)
        for f in fila:
            print(f"{f[0]:^10}{f[1]:^10}")
    else: 
        print("NO HAS SELECCIONADO UN COCHE DISPONIBLE")
    cursor.fetchall()
    conn.commit() 
    conn.close
    