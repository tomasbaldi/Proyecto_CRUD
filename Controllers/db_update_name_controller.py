import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Empleados import Empleados

class db_update_name_controller():

    def __init__(self, db_update_name):
        self.empleados = Empleados(connection())
        self.db_update_name = db_update_name
    
    def actualizar_nombre(self, str_id_empleado, str_upd_name):
        id = [str_id_empleado]
        nombre = [str_upd_name.title()]
        self.empleados.upd_name(id, nombre)
        