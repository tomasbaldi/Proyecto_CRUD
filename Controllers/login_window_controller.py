import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Users import Users

class login_window_controller():
    
    def __init__(self, login):
        self.users = Users(connection())
        self.login = login

    def login_app(self, user, password, Ui_LoginWindow, Ui_main_bd_window):
        datos = self.users.getUser(user, password)
        if datos:
            Ui_LoginWindow.hide()
            self.login.Form = QtWidgets.QMainWindow()
            self.login.ui = Ui_main_bd_window()
            self.login.ui.setupUi(self.login.Form)
            self.login.Form.show()
        else:
            print("Usted no se encuentra registrado")
