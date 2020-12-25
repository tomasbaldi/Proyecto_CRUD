import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Empleados import Empleados

class db_search_controller():

    def __init__(self, db_search):
        self.empleados = Empleados(connection())
        self.db_search = db_search

    def resultados(self, Ui_search_window, Ui_searchresults_window):
        #Ui_main_bd_window.hide()
        self.db_search.Form = QtWidgets.QMainWindow()
        self.db_search.ui = Ui_searchresults_window()
        self.db_search.ui.setupUi(self.db_search.Form)
        self.db_search.Form.show()

    def buscar(self, str_nombre, str_apellido, str_departamento, str_alta_de_empleado_min, str_alta_de_empleado_max, str_sueldo_bruto_min, str_sueldo_bruto_max):
        nombre = [str_nombre]
        apellido = [str_apellido]
        departamento = [str_departamento]
        alta_de_empleado_min = [str_alta_de_empleado_min]
        alta_de_empleado_max = [str_alta_de_empleado_max]
        sueldo_bruto_min = [str_sueldo_bruto_min]
        sueldo_bruto_max = [str_sueldo_bruto_max]
        datos = self.empleados.search(nombre, apellido, departamento, alta_de_empleado_min, alta_de_empleado_max, sueldo_bruto_min, sueldo_bruto_max)
        print(datos)