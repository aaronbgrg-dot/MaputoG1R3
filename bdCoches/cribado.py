import sqlite3

def crear_tabla():
    conn = sqlite3.connect('coches.db')
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE Coches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Marca TEXT NOT NULL,
            Modelo TEXT NOT NULL,
            Año INTEGER NOT NULL,
            Motor TEXT NOT NULL,
            Ruedas TEXT NOT NULL,
            Cambio TEXT NOT NULL,
            Transmision TEXT NOT NULL,
            Chasis TEXT NOT NULL,
            Aceite TEXT NOT NULL,
            Embrague TEXT NOT NULL
            );
    """)
    
    conn.commit()
    conn.close()

def insertar_objetos():
    with open('coches.txt', 'r') as e:
        datos = e.readlines()
    
    for d in datos:
        lDatos = d.split('|')
        
        conn = sqlite3.connect('coches.db')
        cursor = conn.cursor()
        
        cursor.execute(f"""
            INSERT INTO Coches (Marca, Modelo, Año, Motor, Ruedas, Cambio, Transmision, Chasis, Aceite, Embrague)
            VALUES ('{lDatos[0]}', '{lDatos[1]}', {lDatos[2]}, '{lDatos[3]}', '{lDatos[4]}', '{lDatos[5]}', '{lDatos[6]}', '{lDatos[7]}', '{lDatos[8]}', '{lDatos[9]}')
        """)
        
        conn.commit()
        conn.close()

if __name__ == '__main__':
    crear_tabla()
    insertar_objetos()