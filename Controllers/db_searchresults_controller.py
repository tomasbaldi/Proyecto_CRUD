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

    def update_search_table(self, datos):
        self.datos = datos
        self.table = self.db_searchresults.search_empleados_table
        self.table.setRowCount(len(self.datos))
        for fila in range(len(self.datos)):
            for columna in range(len(self.datos[fila])):
                self.table.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(self.datos[fila][columna])))

    def ocultar_ventana(self, Ui_searchresults_window):
        Ui_searchresults_window.hide()