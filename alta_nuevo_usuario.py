import hashlib
import sqlite3

entry_user = input("Ingrese su usuario: ")
entry_password = input("Ingrese su clave: ")

password_cifrada = hashlib.new("sha1", entry_password.encode('utf-8'))

user = [entry_user]
password = [password_cifrada.hexdigest()]
#print(password_cifrada.hexdigest())

try:
    db_connection = sqlite3.connect('.\\Database\\base_nueva.db')
    print("Database connection successfull.")
    db_cursor = db_connection.cursor()
    db_cursor.execute("INSERT INTO users VALUES(?, ?)", user + password)
    db_connection.commit()
    db_connection.close()
    print("Usuario dado de alta satisfactoriamente!")
except:
    print('Error - check Database connection.')






