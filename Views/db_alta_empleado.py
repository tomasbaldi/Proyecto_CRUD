import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Controllers.db_alta_empleado_controller import db_alta_empleado_controller
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class Ui_alta_window(object):
    
    def __init__(self):
        self.alta_empleado_controller = db_alta_empleado_controller(self)

    def setupUi(self, alta_window):
        alta_window.setObjectName("alta_window")
        alta_window.resize(500, 400)
        alta_window.setMinimumSize(QtCore.QSize(500, 400))
        alta_window.setMaximumSize(QtCore.QSize(500, 500))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        alta_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(alta_window)
        self.centralwidget.setObjectName("centralwidget")
        self.alta_main_title = QtWidgets.QLabel(self.centralwidget)
        self.alta_main_title.setGeometry(QtCore.QRect(0, 30, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.alta_main_title.setFont(font)
        self.alta_main_title.setTextFormat(QtCore.Qt.AutoText)
        self.alta_main_title.setAlignment(QtCore.Qt.AlignCenter)
        self.alta_main_title.setObjectName("alta_main_title")
        self.nombre_label = QtWidgets.QLabel(self.centralwidget)
        self.nombre_label.setGeometry(QtCore.QRect(40, 90, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.nombre_label.setFont(font)
        self.nombre_label.setObjectName("nombre_label")
        self.apellido_label = QtWidgets.QLabel(self.centralwidget)
        self.apellido_label.setGeometry(QtCore.QRect(40, 130, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.apellido_label.setFont(font)
        self.apellido_label.setObjectName("apellido_label")
        self.depto_label = QtWidgets.QLabel(self.centralwidget)
        self.depto_label.setGeometry(QtCore.QRect(40, 170, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.depto_label.setFont(font)
        self.depto_label.setObjectName("depto_label")
        self.date_label = QtWidgets.QLabel(self.centralwidget)
        self.date_label.setGeometry(QtCore.QRect(40, 210, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.sueldo_label = QtWidgets.QLabel(self.centralwidget)
        self.sueldo_label.setGeometry(QtCore.QRect(40, 250, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.sueldo_label.setFont(font)
        self.sueldo_label.setObjectName("sueldo_label")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(160, 320, 171, 31))
        self.save_button.setAutoDefault(False)
        self.save_button.setDefault(False)
        self.save_button.setObjectName("save_button")
        self.entry_alta_nombre = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_alta_nombre.setGeometry(QtCore.QRect(230, 90, 201, 20))
        self.entry_alta_nombre.setMaxLength(20)
        self.entry_alta_nombre.setClearButtonEnabled(True)
        self.entry_alta_nombre.setObjectName("entry_alta_nombre")
        self.entry_alta_apellido = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_alta_apellido.setGeometry(QtCore.QRect(230, 130, 201, 20))
        self.entry_alta_apellido.setMaxLength(20)
        self.entry_alta_apellido.setClearButtonEnabled(True)
        self.entry_alta_apellido.setObjectName("entry_alta_apellido")
        self.entry_alta_depto = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_alta_depto.setGeometry(QtCore.QRect(230, 170, 201, 20))
        self.entry_alta_depto.setMaxLength(20)
        self.entry_alta_depto.setClearButtonEnabled(True)
        self.entry_alta_depto.setObjectName("entry_alta_depto")
        self.entry_alta_date = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_alta_date.setGeometry(QtCore.QRect(230, 210, 201, 20))
        self.entry_alta_date.setMaxLength(10)
        self.entry_alta_date.setClearButtonEnabled(True)
        self.entry_alta_date.setObjectName("entry_alta_date")
        self.entry_sueldo_bruto = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_sueldo_bruto.setGeometry(QtCore.QRect(230, 250, 201, 20))
        self.entry_sueldo_bruto.setMaxLength(10)
        self.entry_sueldo_bruto.setClearButtonEnabled(True)
        self.entry_sueldo_bruto.setObjectName("entry_sueldo_bruto")
        alta_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(alta_window)
        QtCore.QMetaObject.connectSlotsByName(alta_window)

        #------------------------------Regex--------------------------------
        self.rx1 = QRegExp("[a-z ]+")
        self.entry_alta_nombre.setValidator(QRegExpValidator(self.rx1))
        self.rx2 = QRegExp("[a-z ]+")
        self.entry_alta_apellido.setValidator(QRegExpValidator(self.rx2))
        self.rx3 = QRegExp("[a-z ]+")
        self.entry_alta_depto.setValidator(QRegExpValidator(self.rx3))
        self.rx4 = QRegExp("[0-9]+")
        self.entry_alta_date.setValidator(QRegExpValidator(self.rx4))
        self.entry_alta_date.setInputMask("9999-99-99")
        self.rx5 = QRegExp("[0-9]+")
        self.entry_sueldo_bruto.setValidator(QRegExpValidator(self.rx5))                
        #------------------------------End Regex----------------------------
        
        #------------------------------Events-------------------------------
        self.x = self.save_button.clicked.connect(lambda:self.alta_empleado_controller.alta_empleado(self.entry_alta_nombre.displayText(), self.entry_alta_apellido.displayText(), self.entry_alta_depto.displayText(), self.entry_alta_date.displayText(), self.entry_sueldo_bruto.displayText()))
        
        self.x = self.save_button.clicked.connect(lambda:self.msg_add_ok())
        
        self.x = self.save_button.clicked.connect(lambda:self.clear_entrys())
        #----------------------------End Events-----------------------------

    def retranslateUi(self, alta_window):
        _translate = QtCore.QCoreApplication.translate
        alta_window.setWindowTitle(_translate("alta_window", "BD Empleados v2.0"))
        self.alta_main_title.setText(_translate("alta_window", "Complete los siguientes campos:"))
        self.nombre_label.setText(_translate("alta_window", "Nombre:"))
        self.apellido_label.setText(_translate("alta_window", "Apellido:"))
        self.depto_label.setText(_translate("alta_window", "Departamento:"))
        self.date_label.setText(_translate("alta_window", "Fecha de alta:"))
        self.sueldo_label.setText(_translate("alta_window", "Sueldo Bruto:"))
        self.save_button.setText(_translate("alta_window", "Dar de alta"))

    def msg_add_ok(self):
        self.msg_upd = QMessageBox()
        self.msg_upd.setIcon(QMessageBox.Information)
        self.msg_upd.setWindowTitle("Estado de alta de empleado")
        self.msg_upd.setText("Se agregó el registro a la base de datos!")
        self.msg_upd.setInformativeText("Presione OK para continuar.")
        self.msg_upd.show()

    def clear_entrys(self):
        self.entry_alta_nombre.clear()
        self.entry_alta_apellido.clear()
        self.entry_alta_depto.clear()
        self.entry_alta_date.clear()
        self.entry_sueldo_bruto.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    alta_window = QtWidgets.QMainWindow()
    ui = Ui_alta_window()
    ui.setupUi(alta_window)
    alta_window.show()
    sys.exit(app.exec_())
