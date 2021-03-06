import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Controllers.db_baja_empleado_controller import db_baja_empleado_controller
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class Ui_baja_window(object):

    def __init__(self):
        self.baja_empleado_controller = db_baja_empleado_controller(self)

    def setupUi(self, baja_window):
        baja_window.setObjectName("baja_window")
        baja_window.resize(500, 300)
        baja_window.setMinimumSize(QtCore.QSize(500, 300))
        baja_window.setMaximumSize(QtCore.QSize(500, 300))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        baja_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(baja_window)
        self.centralwidget.setObjectName("centralwidget")
        self.baja_main_title = QtWidgets.QLabel(self.centralwidget)
        self.baja_main_title.setGeometry(QtCore.QRect(0, 30, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.baja_main_title.setFont(font)
        self.baja_main_title.setTextFormat(QtCore.Qt.AutoText)
        self.baja_main_title.setAlignment(QtCore.Qt.AlignCenter)
        self.baja_main_title.setObjectName("baja_main_title")
        self.idempleado_label = QtWidgets.QLabel(self.centralwidget)
        self.idempleado_label.setGeometry(QtCore.QRect(30, 100, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.idempleado_label.setFont(font)
        self.idempleado_label.setObjectName("idempleado_label")
        self.fechabaja_label = QtWidgets.QLabel(self.centralwidget)
        self.fechabaja_label.setGeometry(QtCore.QRect(30, 150, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.fechabaja_label.setFont(font)
        self.fechabaja_label.setObjectName("fechabaja_label")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(170, 220, 171, 31))
        self.save_button.setAutoDefault(False)
        self.save_button.setDefault(False)
        self.save_button.setObjectName("save_button")
        self.id_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.id_entry.setGeometry(QtCore.QRect(310, 100, 141, 20))
        self.id_entry.setMaxLength(3)
        self.id_entry.setClearButtonEnabled(True)
        self.id_entry.setObjectName("id_entry")
        self.baja_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.baja_entry.setGeometry(QtCore.QRect(310, 150, 141, 20))
        self.baja_entry.setMaxLength(10)
        self.baja_entry.setClearButtonEnabled(True)
        self.baja_entry.setObjectName("baja_entry")
        baja_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(baja_window)
        QtCore.QMetaObject.connectSlotsByName(baja_window)
        
        #------------------------------Regex--------------------------------
        self.rx1 = QRegExp("[0-9]+")
        self.id_entry.setValidator(QRegExpValidator(self.rx1))
        self.rx2 = QRegExp("[0-9]+")
        self.baja_entry.setValidator(QRegExpValidator(self.rx2))
        self.baja_entry.setInputMask("9999-99-99")
        #------------------------------End Regex----------------------------

        #------------------------------Events-------------------------------
        self.x = self.save_button.clicked.connect(lambda:self.baja_empleado_controller.baja_empleado(self.id_entry.displayText(), self.baja_entry.displayText()))
        self.x = self.save_button.clicked.connect(lambda:self.msg_baja_ok())
        self.x = self.save_button.clicked.connect(lambda:self.clear_entrys())
        #----------------------------End Events-----------------------------


    def retranslateUi(self, baja_window):
        _translate = QtCore.QCoreApplication.translate
        baja_window.setWindowTitle(_translate("baja_window", "BD Empleados v2.0"))
        self.baja_main_title.setText(_translate("baja_window", "Complete los siguientes campos:"))
        self.idempleado_label.setText(_translate("baja_window", "Ingrese el ID del empleado:"))
        self.fechabaja_label.setText(_translate("baja_window", "Ingrese la fecha de baja:"))
        self.save_button.setText(_translate("baja_window", "Dar de baja"))

    def msg_baja_ok(self):
        self.msg_upd = QMessageBox()
        self.msg_upd.setIcon(QMessageBox.Information)
        self.msg_upd.setWindowTitle("Estado de baja de empleado")
        self.msg_upd.setText("Se realizó la baja del ID correctamente!")
        self.msg_upd.setInformativeText("Presione OK para continuar.")
        self.msg_upd.show()

    def clear_entrys(self):
        self.id_entry.clear()
        self.baja_entry.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    baja_window = QtWidgets.QMainWindow()
    ui = Ui_baja_window()
    ui.setupUi(baja_window)
    baja_window.show()
    sys.exit(app.exec_())
