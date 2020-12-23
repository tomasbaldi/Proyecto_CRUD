import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.db_update_select_controller import db_update_select_controller


class Ui_select_upd_window(object):

    def __init__(self):
        self.update_select_controller = db_update_select_controller(self)

    def setupUi(self, select_upd_window):
        select_upd_window.setObjectName("select_upd_window")
        select_upd_window.resize(400, 300)
        select_upd_window.setMinimumSize(QtCore.QSize(400, 300))
        select_upd_window.setMaximumSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        select_upd_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(select_upd_window)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.upd_nombre = QtWidgets.QPushButton(self.centralwidget)
        self.upd_nombre.setGeometry(QtCore.QRect(120, 80, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.upd_nombre.setFont(font)
        self.upd_nombre.setAutoDefault(False)
        self.upd_nombre.setObjectName("upd_nombre")
        self.upd_apellido = QtWidgets.QPushButton(self.centralwidget)
        self.upd_apellido.setGeometry(QtCore.QRect(120, 130, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.upd_apellido.setFont(font)
        self.upd_apellido.setAutoDefault(False)
        self.upd_apellido.setObjectName("upd_apellido")
        self.upd_dpto = QtWidgets.QPushButton(self.centralwidget)
        self.upd_dpto.setGeometry(QtCore.QRect(120, 180, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.upd_dpto.setFont(font)
        self.upd_dpto.setAutoDefault(False)
        self.upd_dpto.setObjectName("upd_dpto")
        self.upd_sueldo = QtWidgets.QPushButton(self.centralwidget)
        self.upd_sueldo.setGeometry(QtCore.QRect(120, 230, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.upd_sueldo.setFont(font)
        self.upd_sueldo.setAutoDefault(False)
        self.upd_sueldo.setObjectName("upd_sueldo")
        self.upd_title = QtWidgets.QLabel(self.centralwidget)
        self.upd_title.setGeometry(QtCore.QRect(0, 20, 401, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.upd_title.setFont(font)
        self.upd_title.setTextFormat(QtCore.Qt.AutoText)
        self.upd_title.setAlignment(QtCore.Qt.AlignCenter)
        self.upd_title.setObjectName("upd_title")
        select_upd_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(select_upd_window)
        QtCore.QMetaObject.connectSlotsByName(select_upd_window)

    def retranslateUi(self, select_upd_window):
        _translate = QtCore.QCoreApplication.translate
        select_upd_window.setWindowTitle(_translate("select_upd_window", "BD Empleados v2.0"))
        self.upd_nombre.setText(_translate("select_upd_window", "Nombre"))
        self.upd_apellido.setText(_translate("select_upd_window", "Apellido"))
        self.upd_dpto.setText(_translate("select_upd_window", "Departamento"))
        self.upd_sueldo.setText(_translate("select_upd_window", "Sueldo Bruto"))
        self.upd_title.setText(_translate("select_upd_window", "Seleccione el atributo a modificar:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    select_upd_window = QtWidgets.QMainWindow()
    ui = Ui_select_upd_window()
    ui.setupUi(select_upd_window)
    select_upd_window.show()
    sys.exit(app.exec_())
