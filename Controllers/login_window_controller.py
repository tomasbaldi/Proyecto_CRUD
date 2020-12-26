import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

import hashlib
from PyQt5 import QtWidgets
from Database.Connection import connection
from Models.Users import Users
from PyQt5.QtWidgets import QMessageBox

class login_window_controller():
    
    def __init__(self, login):
        self.users = Users(connection())
        self.login = login

    def login_app(self, user, password, Ui_LoginWindow, Ui_main_bd_window):
        password_encriptada = hashlib.new("sha1", password.encode('utf-8'))
        print("Corroborando credenciales:")
        print("USER = {}".format(user))
        print("PASSWORD = {}".format(password_encriptada.hexdigest()))

        datos = self.users.getUser(user, password_encriptada.hexdigest())
        if datos:
            Ui_LoginWindow.hide()
            self.login.Form = QtWidgets.QMainWindow()
            self.login.ui = Ui_main_bd_window()
            self.login.ui.setupUi(self.login.Form)
            self.login.Form.show()
        else:
            self.msg_upd = QMessageBox()
            self.msg_upd.setIcon(QMessageBox.Information)
            self.msg_upd.setWindowTitle("Error Credenciales")
            self.msg_upd.setText("Usted no se encuentra registado en el sistema.")
            self.msg_upd.setInformativeText("Comuniquese con un administrador para dar de alta un nuevo usuario.")
            self.msg_upd.show()
