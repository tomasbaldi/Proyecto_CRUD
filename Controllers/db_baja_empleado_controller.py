import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Empleados import Empleados

class db_baja_empleado_controller():

    def __init__(self, db_baja_empleado):
        self.empleados = Empleados(connection())
        self.db_baja_empleado = db_baja_empleado

    def baja_empleado(self, str_id, str_date_baja):
        id = [str_id]
        fecha_baja = [str_date_baja]
        self.empleados.remove_empleado(id, fecha_baja)