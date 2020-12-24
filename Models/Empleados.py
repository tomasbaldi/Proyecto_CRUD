class Empleados():
    
    def __init__(self, db_connection):
        
        try:
            self.db_connection = db_connection
            self.db_cursor = self.db_connection.cursor()
            self.db_cursor.execute("""CREATE TABLE empleados (
                                                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                                        nombre TEXT NOT NULL,
                                                        apellido TEXT NOT NULL,
                                                        departamento TEXT NOT NULL,
                                                        alta_de_empleado TEXT NOT NULL,
                                                        sueldo_bruto TEXT NOT NULL,
                                                        baja_de_empleado TEXT
                                    )""")
            self.db_connection.commit()
            self.db_connection.close()
            print("empleados table created successfully")
        
        except:
            print('empleados table already exists')