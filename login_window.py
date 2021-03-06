import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.login_window_controller import login_window_controller
from PyQt5.QtWidgets import QMessageBox
from Views.db_mainwindow import Ui_main_bd_window
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class Ui_LoginWindow(object):

    def __init__(self):
        self.login_window_controller = login_window_controller(self)

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.setWindowModality(QtCore.Qt.NonModal)
        LoginWindow.resize(450, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QtCore.QSize(450, 300))
        LoginWindow.setMaximumSize(QtCore.QSize(450, 300))
        LoginWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.top_title = QtWidgets.QLabel(self.centralwidget)
        self.top_title.setGeometry(QtCore.QRect(0, 40, 451, 21))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.top_title.setFont(font)
        self.top_title.setTextFormat(QtCore.Qt.PlainText)
        self.top_title.setAlignment(QtCore.Qt.AlignCenter)
        self.top_title.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.top_title.setObjectName("top_title")
        self.middle_title = QtWidgets.QLabel(self.centralwidget)
        self.middle_title.setGeometry(QtCore.QRect(0, 100, 451, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middle_title.sizePolicy().hasHeightForWidth())
        self.middle_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.middle_title.setFont(font)
        self.middle_title.setTextFormat(QtCore.Qt.PlainText)
        self.middle_title.setAlignment(QtCore.Qt.AlignCenter)
        self.middle_title.setObjectName("middle_title")
        self.user_title = QtWidgets.QLabel(self.centralwidget)
        self.user_title.setGeometry(QtCore.QRect(50, 160, 151, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_title.sizePolicy().hasHeightForWidth())
        self.user_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.user_title.setFont(font)
        self.user_title.setTextFormat(QtCore.Qt.PlainText)
        self.user_title.setAlignment(QtCore.Qt.AlignCenter)
        self.user_title.setObjectName("user_title")
        self.pwd_title = QtWidgets.QLabel(self.centralwidget)
        self.pwd_title.setGeometry(QtCore.QRect(50, 190, 151, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwd_title.sizePolicy().hasHeightForWidth())
        self.pwd_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.pwd_title.setFont(font)
        self.pwd_title.setTextFormat(QtCore.Qt.PlainText)
        self.pwd_title.setAlignment(QtCore.Qt.AlignCenter)
        self.pwd_title.setObjectName("pwd_title")
        self.enter_button = QtWidgets.QPushButton(self.centralwidget)
        self.enter_button.setGeometry(QtCore.QRect(170, 240, 120, 23))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.enter_button.setFont(font)
        self.enter_button.setCheckable(False)
        self.enter_button.setChecked(False)
        self.enter_button.setAutoDefault(False)
        self.enter_button.setDefault(True)
        self.enter_button.setObjectName("enter_button")
        self.user_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.user_entry.setGeometry(QtCore.QRect(210, 160, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.user_entry.setFont(font)
        self.user_entry.setMaxLength(12)
        self.user_entry.setClearButtonEnabled(True)
        self.user_entry.setObjectName("user_entry")
        self.pwd_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.pwd_entry.setGeometry(QtCore.QRect(210, 190, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.pwd_entry.setFont(font)
        self.pwd_entry.setMaxLength(6)
        self.pwd_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd_entry.setClearButtonEnabled(True)
        self.pwd_entry.setObjectName("pwd_entry")
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)
        
        #------------------------------Regex--------------------------------
        self.rx1 = QRegExp("[a-z]+")
        self.user_entry.setValidator(QRegExpValidator(self.rx1))
        self.rx2 = QRegExp("[0-9]+")
        self.pwd_entry.setValidator(QRegExpValidator(self.rx2))
        #------------------------------End Regex----------------------------
        
        #------------------------------Events-------------------------------
        self.x = self.enter_button.clicked.connect(lambda:self.login_window_controller.login_app(self.user_entry.text(), self.pwd_entry.text(), LoginWindow, Ui_main_bd_window))
        #----------------------------End Events-----------------------------

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "BD Empleados v2.0"))
        self.top_title.setText(_translate("LoginWindow", "Bienvenido a BD Empleados!"))
        self.middle_title.setText(_translate("LoginWindow", "Ingrese a continuación su usuario y contraseña:"))
        self.user_title.setText(_translate("LoginWindow", "Usuario:"))
        self.pwd_title.setText(_translate("LoginWindow", "Contraseña:"))
        self.enter_button.setText(_translate("LoginWindow", "Ingresar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())
