import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Empleados import Empleados

class db_update_depto_controller():

    def __init__(self, db_update_depto):
        self.empleados = Empleados(connection())
        self.db_update_depto = db_update_depto
           
    def actualizar_depto(self, str_id_empleado, str_upd_depto):
        id = [str_id_empleado]
        departamento = [str_upd_depto]
        self.empleados.upd_depto(id, departamento)
        