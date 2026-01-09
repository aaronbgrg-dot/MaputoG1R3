import sqlite3

def insertar_coches():
    with open('./bdCoches/coches.txt', 'r') as e:
        datos = e.readlines()
    
    for d in datos:
        lDatos = d.split('|')
        
        conn = sqlite3.connect('Maputo S.L..db')
        cursor = conn.cursor()
        
        cursor.execute(f"""
            INSERT INTO coches (Marca, Modelo, Año, Motor, Ruedas, Cambio, Transmisión, Chasis, Aceite, Embrague)
            VALUES ('{lDatos[0]}', '{lDatos[1]}', {lDatos[2]}, '{lDatos[3]}', '{lDatos[4]}', '{lDatos[5]}', '{lDatos[6]}', '{lDatos[7]}', '{lDatos[8]}', '{lDatos[9]}')
        """)
        
        conn.commit()
        conn.close()

if __name__ == '__main__':
    insertar_coches()