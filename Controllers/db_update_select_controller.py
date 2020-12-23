import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Empleados import Empleados

class db_update_select_controller():

    def __init__(self, db_update_select):
        self.empleados = Empleados(connection())
        self.db_update_select = db_update_select