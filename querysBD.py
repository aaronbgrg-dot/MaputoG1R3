import sqlite3 as sql

#constante con el str del nombre de la base de datos
BASE = 'Maputo_SL.db'

def solicitarErrores():
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    coche = int(input("De que coche quieres sacar los errores? "))
    if coche < 6 and coche >0 :
        cursor.execute(f"SELECT Id_Error as Error, Id_Coche as Coche, Motivo FROM error WHERE Id_Coche = {coche}")
        fila = cursor.fetchall()
        print("{(Id_Error:, Id_Coche:, Motivo: )}")
        print(fila)
    else: 
        print("NO HAS SELECCIONADO UN COCHE DISPONIBLE")
    cursor.fetchall()
    conn.commit() 
    conn.close

def contadorErroes():
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    coche = int(input("De que coche quieres sacar los errores? "))
    if coche < 6 and coche >0 :
        cursor.execute(f"SELECT Id_Coche as Coche, SUM(Contador) as contador FROM error WHERE Id_Coche = {coche}")
        fila = cursor.fetchall()
        print("[(Coche:, Contador:)]")
        print(fila)
    else: 
        print("NO HAS SELECCIONADO UN COCHE DISPONIBLE")
    cursor.fetchall()
    conn.commit() 
    conn.close
    