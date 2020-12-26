import sqlite3

#CONECTA CON BASE DE DATOS

def connection():
    try:
        db_connection = sqlite3.connect('.\\Database\\base_nueva.db')
        print("Database connection successfull.")
        return db_connection
        
    except:
        print('Error - check Database connection.')
