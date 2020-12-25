import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Empleados import Empleados

class db_alta_empleado_controller():

    def __init__(self, db_alta_empleado):
        self.empleados = Empleados(connection())
        self.db_alta_empleado = db_alta_empleado

    def alta_empleado(self, str_nombre_alta, str_apellido_alta, str_depto_alta, str_date_alta, str_sueldo_alta):
        nombre = [str_nombre_alta]
        apellido = [str_apellido_alta]
        departamento = [str_depto_alta]
        fecha_alta = [str_date_alta]
        sueldo = [str_sueldo_alta]
        self.empleados.add_empleado(nombre, apellido, departamento, fecha_alta, sueldo)