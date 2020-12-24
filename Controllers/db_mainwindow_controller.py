import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Empleados import Empleados

class db_mainwindow_controller():

    #------------------Redireccion a otras ventanas-------------------

    def __init__(self, db_mainwindow):
        self.empleados = Empleados(connection())
        self.db_mainwindow = db_mainwindow

    def add(self, Ui_main_bd_window, Ui_alta_window):
        #Ui_main_bd_window.hide()
        self.db_mainwindow.Form = QtWidgets.QMainWindow()
        self.db_mainwindow.ui = Ui_alta_window()
        self.db_mainwindow.ui.setupUi(self.db_mainwindow.Form)
        self.db_mainwindow.Form.show()
    
    def update(self, Ui_main_bd_window, Ui_select_upd_window):
        #Ui_main_bd_window.hide()
        self.db_mainwindow.Form = QtWidgets.QMainWindow()
        self.db_mainwindow.ui = Ui_select_upd_window()
        self.db_mainwindow.ui.setupUi(self.db_mainwindow.Form)
        self.db_mainwindow.Form.show()
    
    def baja(self, Ui_main_bd_window, Ui_baja_window):
        #Ui_main_bd_window.hide()
        self.db_mainwindow.Form = QtWidgets.QMainWindow()
        self.db_mainwindow.ui = Ui_baja_window()
        self.db_mainwindow.ui.setupUi(self.db_mainwindow.Form)
        self.db_mainwindow.Form.show()

    # def consulta(self, Ui_main_bd_window, Ui_select_upd_window):
    #     #Ui_main_bd_window.hide()
    #     self.db_mainwindow.Form = QtWidgets.QMainWindow()
    #     self.db_mainwindow.ui = Ui_select_upd_window()
    #     self.db_mainwindow.ui.setupUi(self.db_mainwindow.Form)
    #     self.db_mainwindow.Form.show()
    
    def deshacer(self, Ui_main_bd_window, Ui_undo_baja_window):
        #Ui_main_bd_window.hide()
        self.db_mainwindow.Form = QtWidgets.QMainWindow()
        self.db_mainwindow.ui = Ui_undo_baja_window()
        self.db_mainwindow.ui.setupUi(self.db_mainwindow.Form)
        self.db_mainwindow.Form.show()

    def eliminar(self, Ui_main_bd_window, Ui_delete_window):
        #Ui_main_bd_window.hide()
        self.db_mainwindow.Form = QtWidgets.QMainWindow()
        self.db_mainwindow.ui = Ui_delete_window()
        self.db_mainwindow.ui.setupUi(self.db_mainwindow.Form)
        self.db_mainwindow.Form.show()

    #--------------------Actualizacion de tablas-----------------------
    
    def update_table_activos(self):
        self.datos = self.empleados.get_table_activos()
        self.table = self.db_mainwindow.tabla_empleados_activos
        self.table.setRowCount(len(self.datos))
        for fila in range(len(self.datos)):
            for columna in range(len(self.datos[fila])):
                self.table.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(self.datos[fila][columna])))

    def update_table_inactivos(self):
        self.datos = self.empleados.get_table_inactivos()
        self.table = self.db_mainwindow.tabla_empleados_inactivos
        self.table.setRowCount(len(self.datos))
        for fila in range(len(self.datos)):
            for columna in range(len(self.datos[fila])):
                self.table.setItem(fila, columna, QtWidgets.QTableWidgetItem(str(self.datos[fila][columna])))
    
