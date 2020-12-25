import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Empleados import Empleados

class db_undo_empleado_controller():

    def __init__(self, db_undo_empleado):
        self.empleados = Empleados(connection())
        self.db_undo_empleado = db_undo_empleado

    def deshacer_empleado(self, str_id):
        id = [str_id]
        self.empleados.undo_empleado(id)