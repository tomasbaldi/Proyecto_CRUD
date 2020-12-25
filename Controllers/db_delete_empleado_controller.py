import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Empleados import Empleados

class db_delete_empleado_controller():

    def __init__(self, db_delete_empleado):
        self.empleados = Empleados(connection())
        self.db_delete_empleado = db_delete_empleado

    def eliminar_empleado(self, str_id):
        id = [str_id]
        self.empleados.delete_empleado(id)
