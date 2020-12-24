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

    def actualizar_nombre(self, Ui_select_upd_window, Ui_update_nombre_window):
        #Ui_main_bd_window.hide()
        self.db_update_select.Form = QtWidgets.QMainWindow()
        self.db_update_select.ui = Ui_update_nombre_window()
        self.db_update_select.ui.setupUi(self.db_update_select.Form)
        self.db_update_select.Form.show()

    def actualizar_apellido(self, Ui_select_upd_window, Ui_update_apellido_window):
        #Ui_main_bd_window.hide()
        self.db_update_select.Form = QtWidgets.QMainWindow()
        self.db_update_select.ui = Ui_update_apellido_window()
        self.db_update_select.ui.setupUi(self.db_update_select.Form)
        self.db_update_select.Form.show()
    
    def actualizar_departamento(self, Ui_select_upd_window, Ui_update_depto_window):
        #Ui_main_bd_window.hide()
        self.db_update_select.Form = QtWidgets.QMainWindow()
        self.db_update_select.ui = Ui_update_depto_window()
        self.db_update_select.ui.setupUi(self.db_update_select.Form)
        self.db_update_select.Form.show()
    
    def actualizar_sueldo_bruto(self, Ui_select_upd_window, Ui_update_salary_window):
        #Ui_main_bd_window.hide()
        self.db_update_select.Form = QtWidgets.QMainWindow()
        self.db_update_select.ui = Ui_update_salary_window()
        self.db_update_select.ui.setupUi(self.db_update_select.Form)
        self.db_update_select.Form.show()