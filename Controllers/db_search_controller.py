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