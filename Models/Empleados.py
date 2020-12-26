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
            pass
    
    def get_table_activos(self):
        self.db_cursor.execute("""SELECT 
                                        id, 
                                        nombre, 
                                        apellido, 
                                        departamento, 
                                        alta_de_empleado, 
                                        sueldo_bruto 
                                        FROM empleados 
                                        WHERE baja_de_empleado IS NULL ORDER BY apellido ASC
                                """)
        result = self.db_cursor.fetchall()
        
        return result

    def get_table_inactivos(self):
        self.db_cursor.execute("""SELECT 
                                        id, 
                                        nombre, 
                                        apellido, 
                                        departamento, 
                                        alta_de_empleado, 
                                        sueldo_bruto 
                                        FROM empleados 
                                        WHERE baja_de_empleado IS NOT NULL ORDER BY apellido ASC
                                """)
        result = self.db_cursor.fetchall()

        return result

    def search(self, nombre, apellido, departamento, alta_de_empleado_min, alta_de_empleado_max, sueldo_bruto_min, sueldo_bruto_max):
        self.db_cursor.execute("""SELECT * FROM empleados WHERE 
                                                                nombre = ? OR 
                                                                apellido = ? OR 
                                                                departamento = ? OR 
                                                                alta_de_empleado BETWEEN ? AND ? OR 
                                                                sueldo_bruto BETWEEN ? AND ?""", nombre + apellido + departamento + alta_de_empleado_min + alta_de_empleado_max + sueldo_bruto_min + sueldo_bruto_max)
        result = self.db_cursor.fetchall()

        return result

    def add_empleado(self, nombre, apellido, departamento, fecha_alta, sueldo):
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute("INSERT INTO empleados VALUES(NULL, ?, ?, ?, ?, ?, NULL)", nombre + apellido + departamento + fecha_alta + sueldo)
        self.db_connection.commit()
        print("Empleado {} {} agregado correctamente a la base de datos".format(nombre[0], apellido[0]))

    def remove_empleado(self, id, fecha_baja):
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute("UPDATE empleados SET baja_de_empleado = ? WHERE id = ?", fecha_baja + id)
        self.db_connection.commit()
        print("El empleado ID = {} ha sido dado de baja".format(id[0]))

    def delete_empleado(self, id):
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute("DELETE FROM empleados WHERE id = ?", id)
        self.db_connection.commit()
        print("El empleado ID = {} ha sido removido de la base de datos".format(id[0]))

    def undo_empleado(self, id):
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute("UPDATE empleados SET baja_de_empleado = NULL WHERE id = ?", id)
        self.db_connection.commit()
        print("El empleado ID = {} ha sido reincorporado".format(id[0]))

    def upd_name(self, id, nombre):
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute("UPDATE empleados SET nombre = ? WHERE id = ?", nombre + id)
        self.db_connection.commit()
        print("Al empleado ID = {} se le ha modificado el nombre a: {}".format(id[0], nombre[0]))

    def upd_surname(self, id, apellido):
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute("UPDATE empleados SET apellido = ? WHERE id = ?", apellido + id)
        self.db_connection.commit()
        print("Al empleado ID = {} se le ha modificado el apellido a: {}".format(id[0], apellido[0]))
    
    def upd_depto(self, id, departamento):
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute("UPDATE empleados SET departamento = ? WHERE id = ?", departamento + id)
        self.db_connection.commit()
        print("El empleado ID = {} ha sido reasignado al departamento: {}".format(id[0], departamento[0]))

    def upd_salary(self, id, salario):
        self.db_cursor = self.db_connection.cursor()
        self.db_cursor.execute("UPDATE empleados SET sueldo_bruto = ? WHERE id = ?", salario + id)
        self.db_connection.commit()
        print("Al empleado ID = {} se le ha asignado un sueldo bruto de: {}".format(id[0], salario[0]))
        
        

            
