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