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