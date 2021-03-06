import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Controllers.db_update_depto_controller import db_update_depto_controller
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class Ui_update_depto_window(object):

    def __init__(self):
        self.update_depto_controller = db_update_depto_controller(self)

    def setupUi(self, update_depto_window):
        update_depto_window.setObjectName("update_depto_window")
        update_depto_window.resize(500, 300)
        update_depto_window.setMinimumSize(QtCore.QSize(500, 300))
        update_depto_window.setMaximumSize(QtCore.QSize(500, 300))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        update_depto_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(update_depto_window)
        self.centralwidget.setObjectName("centralwidget")
        self.upd_depto_maintitle = QtWidgets.QLabel(self.centralwidget)
        self.upd_depto_maintitle.setGeometry(QtCore.QRect(0, 30, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.upd_depto_maintitle.setFont(font)
        self.upd_depto_maintitle.setTextFormat(QtCore.Qt.AutoText)
        self.upd_depto_maintitle.setAlignment(QtCore.Qt.AlignCenter)
        self.upd_depto_maintitle.setObjectName("upd_depto_maintitle")
        self.idempleado_label = QtWidgets.QLabel(self.centralwidget)
        self.idempleado_label.setGeometry(QtCore.QRect(30, 100, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.idempleado_label.setFont(font)
        self.idempleado_label.setObjectName("idempleado_label")
        self.upd_depto_label = QtWidgets.QLabel(self.centralwidget)
        self.upd_depto_label.setGeometry(QtCore.QRect(30, 140, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.upd_depto_label.setFont(font)
        self.upd_depto_label.setObjectName("upd_depto_label")
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
        self.upd_depto_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.upd_depto_entry.setGeometry(QtCore.QRect(310, 150, 141, 20))
        self.upd_depto_entry.setMaxLength(20)
        self.upd_depto_entry.setClearButtonEnabled(True)
        self.upd_depto_entry.setObjectName("upd_depto_entry")
        update_depto_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(update_depto_window)
        QtCore.QMetaObject.connectSlotsByName(update_depto_window)

        #------------------------------Regex--------------------------------
        self.rx1 = QRegExp("[0-9]+")
        self.id_entry.setValidator(QRegExpValidator(self.rx1))
        self.rx2 = QRegExp("[a-z ]+")
        self.upd_depto_entry.setValidator(QRegExpValidator(self.rx2))
        #------------------------------End Regex----------------------------        
        
        #------------------------------Events-------------------------------
        self.x = self.save_button.clicked.connect(lambda:self.update_depto_controller.actualizar_depto(self.id_entry.displayText(), self.upd_depto_entry.displayText()))
        self.x = self.save_button.clicked.connect(lambda:self.msg_upd_ok())
        self.x = self.save_button.clicked.connect(lambda:self.clear_entrys())
        #----------------------------End Events-----------------------------

    def retranslateUi(self, update_depto_window):
        _translate = QtCore.QCoreApplication.translate
        update_depto_window.setWindowTitle(_translate("update_depto_window", "BD Empleados v2.0"))
        self.upd_depto_maintitle.setText(_translate("update_depto_window", "Complete los siguientes campos:"))
        self.idempleado_label.setText(_translate("update_depto_window", "Ingrese el ID del empleado:"))
        self.upd_depto_label.setText(_translate("update_depto_window", "<html><head/><body><p>Ingrese un nuevo departamento<br/>para el ID ingresado:</p></body></html>"))
        self.save_button.setText(_translate("update_depto_window", "Aplicar cambios"))

    def msg_upd_ok(self):
        self.msg_upd = QMessageBox()
        self.msg_upd.setIcon(QMessageBox.Information)
        self.msg_upd.setWindowTitle("Modificación de departamento")
        self.msg_upd.setText("El valor se actualizó correctamente!")
        self.msg_upd.setInformativeText("Presione OK para continuar.")
        self.msg_upd.show()

    def clear_entrys(self):
        self.id_entry.clear()
        self.upd_depto_entry.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_depto_window = QtWidgets.QMainWindow()
    ui = Ui_update_depto_window()
    ui.setupUi(update_depto_window)
    update_depto_window.show()
    sys.exit(app.exec_())
