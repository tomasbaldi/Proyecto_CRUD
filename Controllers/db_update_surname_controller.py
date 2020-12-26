import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Empleados import Empleados

class db_update_surname_controller():

    def __init__(self, db_update_surname):
        self.empleados = Empleados(connection())
        self.db_update_surname = db_update_surname

    def actualizar_apellido(self, str_id_empleado, str_upd_surname):
        id = [str_id_empleado]
        apellido = [str_upd_surname.title()]
        self.empleados.upd_surname(id, apellido)
