import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Controllers.db_update_salary_controller import db_update_salary_controller
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator


class Ui_update_salary_window(object):

    def __init__(self):
        self.update_salary_controller = db_update_salary_controller(self)

    def setupUi(self, update_salary_window):
        update_salary_window.setObjectName("update_salary_window")
        update_salary_window.resize(500, 300)
        update_salary_window.setMinimumSize(QtCore.QSize(500, 300))
        update_salary_window.setMaximumSize(QtCore.QSize(500, 300))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        update_salary_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(update_salary_window)
        self.centralwidget.setObjectName("centralwidget")
        self.upd_salary_maintitle = QtWidgets.QLabel(self.centralwidget)
        self.upd_salary_maintitle.setGeometry(QtCore.QRect(0, 30, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.upd_salary_maintitle.setFont(font)
        self.upd_salary_maintitle.setTextFormat(QtCore.Qt.AutoText)
        self.upd_salary_maintitle.setAlignment(QtCore.Qt.AlignCenter)
        self.upd_salary_maintitle.setObjectName("upd_salary_maintitle")
        self.idempleado_label = QtWidgets.QLabel(self.centralwidget)
        self.idempleado_label.setGeometry(QtCore.QRect(30, 100, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.idempleado_label.setFont(font)
        self.idempleado_label.setObjectName("idempleado_label")
        self.upd_salary_label = QtWidgets.QLabel(self.centralwidget)
        self.upd_salary_label.setGeometry(QtCore.QRect(30, 140, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.upd_salary_label.setFont(font)
        self.upd_salary_label.setObjectName("upd_salary_label")
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
        self.upd_salary_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.upd_salary_entry.setGeometry(QtCore.QRect(310, 150, 141, 20))
        self.upd_salary_entry.setMaxLength(10)
        self.upd_salary_entry.setClearButtonEnabled(True)
        self.upd_salary_entry.setObjectName("upd_salary_entry")
        update_salary_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(update_salary_window)
        QtCore.QMetaObject.connectSlotsByName(update_salary_window)

        #------------------------------Regex--------------------------------
        self.rx1 = QRegExp("[0-9]+")
        self.id_entry.setValidator(QRegExpValidator(self.rx1))
        self.rx2 = QRegExp("[a-z ]+")
        self.upd_salary_entry.setValidator(QRegExpValidator(self.rx2))
        #------------------------------End Regex----------------------------
        
        #------------------------------Events-------------------------------
        self.x = self.save_button.clicked.connect(lambda:self.update_salary_controller.actualizar_salario(self.id_entry.displayText(), self.upd_salary_entry.displayText()))
        self.x = self.save_button.clicked.connect(lambda:self.msg_upd_ok())
        self.x = self.save_button.clicked.connect(lambda:self.clear_entrys())
        #----------------------------End Events-----------------------------

    def retranslateUi(self, update_salary_window):
        _translate = QtCore.QCoreApplication.translate
        update_salary_window.setWindowTitle(_translate("update_salary_window", "BD Empleados v2.0"))
        self.upd_salary_maintitle.setText(_translate("update_salary_window", "Complete los siguientes campos:"))
        self.idempleado_label.setText(_translate("update_salary_window", "Ingrese el ID del empleado:"))
        self.upd_salary_label.setText(_translate("update_salary_window", "<html><head/><body><p>Ingrese un nuevo sueldo<br/>para el ID ingresado:</p></body></html>"))
        self.save_button.setText(_translate("update_salary_window", "Aplicar cambios"))

    def msg_upd_ok(self):
        self.msg_upd = QMessageBox()
        self.msg_upd.setIcon(QMessageBox.Information)
        self.msg_upd.setWindowTitle("Modificación de sueldo bruto")
        self.msg_upd.setText("El valor se actualizó correctamente!")
        self.msg_upd.setInformativeText("Presione OK para continuar.")
        self.msg_upd.show()

    def clear_entrys(self):
        self.id_entry.clear()
        self.upd_salary_entry.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_salary_window = QtWidgets.QMainWindow()
    ui = Ui_update_salary_window()
    ui.setupUi(update_salary_window)
    update_salary_window.show()
    sys.exit(app.exec_())
