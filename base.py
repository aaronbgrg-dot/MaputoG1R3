import sqlite3 as sql



def crearBD():
    conn = sql.connect("Maputo S.L..db")
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreing_keys = ON;')
    conn.commit()
    conn.close()
    

def tablaCoche():
    conn = sql.connect("Maputo S.L..db")
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreing_keys = ON;')
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
    conn = sql.connect("Maputo S.L..db")
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreing_keys = ON;')
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
    conn = sql.connect("Maputo S.L..db")
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreing_keys = ON;')
    cursor.execute(
        

        """CREATE TABLE montaje(
            Id_Mont INTEGER PRIMARY KEY AUTOINCREMENT,
            Id_Coche INTEGER NOT NULL,
            Horas INTEGER,
            PrecioHora INTEGER,
            foreign key (Id_Coche) references coches(Id_Coche)                         
        )"""
        )
    
def tablaPintado():
    conn = sql.connect("Maputo S.L..db")
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreing_keys = ON;')
    cursor.execute(
        

        """CREATE TABLE pintado(
            Id_Pint INTEGER PRIMARY KEY AUTOINCREMENT,
            Id_Coche INTEGER NOT NULL,
            Horas INTEGER,
            PrecioHora INTEGER,
            foreign key (Id_Coche) references coches(Id_Coche)                         
        )"""
        )
    
def tablaAcabado():
    conn = sql.connect("Maputo S.L..db")
    cursor = conn.cursor()
    cursor.execute('PRAGMA foreing_keys = ON;')
    cursor.execute(
        

        """CREATE TABLE acabado(
            Id_Acab INTEGER PRIMARY KEY AUTOINCREMENT,
            Id_Coche INTEGER NOT NULL,
            Horas INTEGER,
            PrecioHora INTEGER,
            foreign key (Id_Coche) references coches(Id_Coche)                         
        )"""
        )

    conn.commit()
    conn.close()           

def base():
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