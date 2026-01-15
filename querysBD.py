import sqlite3 as sql

#constante con el str del nombre de la base de datos
BASE = 'Maputo_SL.db'

def solicitarErrores():
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    coche = int(input("De que coche quieres sacar los errores? "))
    if coche < 6 and coche >0 :
        cursor.execute(f"SELECT Id_Error as Error, Id_Coche as Coche, SUM(Contador) as contador, Motivo FROM error WHERE Id_Coche = {coche}")
        fila = cursor.fetchall()
        print(fila)
    else: 
        print("NO HAS SELECCIONADO UN COCHE DISPONIBLE")
    cursor.fetchall()
    conn.commit() 
    conn.close
