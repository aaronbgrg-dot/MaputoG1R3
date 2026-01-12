import sqlite3

BASE = 'Maputo_SL.db'

def insertar_coches():
    #Abre el archivo de texto coches.txt
    #Lee las líneas del archivo
    with open('./bdCoches/coches.txt', 'r') as e:
        datos = e.readlines()
    
    for d in datos:
        #Separa los elementos
        lDatos = d.split('|')
        
        #Añade los elementos a la tabla coches de la base de datos Maputo S.L.
        conn = sqlite3.connect(BASE)
        cursor = conn.cursor()
        
        cursor.execute(f"""
            INSERT INTO coches (Marca, Modelo, Año, Motor, Ruedas, Cambio, Transmisión, Chasis, Aceite, Embrague)
            VALUES ('{lDatos[0]}', '{lDatos[1]}', {lDatos[2]}, '{lDatos[3]}', '{lDatos[4]}', '{lDatos[5]}', '{lDatos[6]}', '{lDatos[7]}', '{lDatos[8]}', '{lDatos[9]}')
        """)
        
        conn.commit()
        conn.close()

if __name__ == '__main__':
    insertar_coches()