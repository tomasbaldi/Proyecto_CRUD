import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Empleados import Empleados

class db_searchresults_controller():

    def __init__(self, db_searchresults):
        self.empleados = Empleados(connection())
        self.db_searchresults = db_searchresults