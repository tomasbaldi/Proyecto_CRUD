import sqlite3

#CONECTA CON BASE DE DATOS

def connection():
    try:
        db_connection = sqlite3.connect('.\\Database\\base_nueva.db')
        print("database connection successfully")
        return db_connection
        
    except:
        print('database already exist')
    
#CREA TABLA EMPLEADOS

def create_table_empleados(db_connection):
    try:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""CREATE TABLE empleados (
                                                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                                                    nombre TEXT NOT NULL,
                                                    apellido TEXT NOT NULL,
                                                    departamento TEXT NOT NULL,
                                                    alta_de_empleado TEXT NOT NULL,
                                                    sueldo_bruto TEXT NOT NULL,
                                                    baja_de_empleado TEXT
                        )""")
        db_connection.commit()
        db_connection.close()
        print("empleados table created successfully")

    except:
        print('empleados table already exist')

#CREA TABLA USERS

def create_table_users(db_connection):
    try:
        db_cursor = db_connection.cursor()
        db_cursor.execute("""CREATE TABLE users (
                                                    user TEXT NOT NULL PRIMARY KEY UNIQUE,
                                                    password TEXT NOT NULL
                        )""")
        db_connection.commit()
        db_connection.close()
        print("users table created successfully")

    except:
        print('users table already exist')

con = connection()
create_table_empleados(con)
create_table_users(con)
