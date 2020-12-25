import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Empleados import Empleados

class db_update_salary_controller():

    def __init__(self, db_update_salary):
        self.empleados = Empleados(connection())
        self.db_update_salary = db_update_salary

    def actualizar_salario(self, str_id_empleado, str_upd_salary):
        id = [str_id_empleado]
        salario = [str_upd_salary]
        self.empleados.upd_salary(id, salario)