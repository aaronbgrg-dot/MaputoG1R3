import sqlite3 as sql


BASE = 'Maputo_SL.db'

def crearBD():
    # Crea la base de datos
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreing_keys = ON;')
    conn.commit()
    conn.close()

def tablaCoche():
    # Se conecta a la base de datos
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreing_keys = ON;')
    # Crea la tabla "coches"
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS coches(
            Id_Coche INTEGER PRIMARY KEY AUTOINCREMENT,
            Marca text,
            Modelo text,
            Año Integer,
            Motor text,
            Ruedas text,
            Cambio text,
            Transmisión text,
            Chasis text,
            Aceite text,
            Embrague text
        )"""
    )
    conn.commit()
    conn.close()

def tablaError():
    # Se conecta a la base de datos
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreing_keys = ON;')
    # Crea la tabla error
    cursor.execute(
        """CREATE TABLE error(
            Id_Error INTEGER PRIMARY KEY AUTOINCREMENT,
            Id_Coche INTEGER NOT NULL,
            Contador INTEGER,
            Motivo text,
            foreign key (Id_Coche) references coches(Id_Coche)                         
        )"""
        )
    conn.commit()
    conn.close()

def tablaMontaje():
    # Se conecta a la base de datos
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreing_keys = ON;')
    # Crea la tabla "montaje"
    cursor.execute(
        """CREATE TABLE montaje(
            Id_Mont INTEGER PRIMARY KEY AUTOINCREMENT,
            Id_Coche INTEGER NOT NULL,
            Horas INTEGER,
            PrecioHora INTEGER,
            Status text,
            foreign key (Id_Coche) references coches(Id_Coche)                         
        )"""
        )
    

def tablaPintado():
    # Se conecta a la base de datos
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreing_keys = ON;')
    # Crea la tabla "pintado"
    cursor.execute(
        """CREATE TABLE pintado(
            Id_Pint INTEGER PRIMARY KEY AUTOINCREMENT,
            Id_Coche INTEGER NOT NULL,
            Horas INTEGER,
            PrecioHora INTEGER,
            Status text,
            foreign key (Id_Coche) references coches(Id_Coche)                         
        )"""
        )

def tablaAcabado():
    # Se conecta a la base de datos
    conn = sql.connect(BASE)
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreing_keys = ON;')
    # Crea la tabla "acabado"
    cursor.execute(
        """CREATE TABLE acabado(
            Id_Acab INTEGER PRIMARY KEY AUTOINCREMENT,
            Id_Coche INTEGER NOT NULL,
            Horas INTEGER,
            PrecioHora INTEGER,
            Status text,
            foreign key (Id_Coche) references coches(Id_Coche)                         
        )"""
        )
    conn.commit()
    conn.close()           

def base():
    # Ejecuta todas las funciones anteriores
    crearBD()
    tablaCoche()
    tablaError()
    tablaAcabado()
    tablaMontaje()
    tablaPintado()



if __name__ == "__main__":
    crearBD()
    tablaCoche()
    tablaError()
    tablaAcabado()
    tablaMontaje()
    tablaPintado()