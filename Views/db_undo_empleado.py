import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from Controllers.db_undo_empleado_controller import db_undo_empleado_controller
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class Ui_undo_baja_window(object):
    
    def __init__(self):
        self.undo_empleado_controller = db_undo_empleado_controller(self)

    def setupUi(self, undo_baja_window):
        undo_baja_window.setObjectName("undo_baja_window")
        undo_baja_window.resize(500, 250)
        undo_baja_window.setMinimumSize(QtCore.QSize(500, 250))
        undo_baja_window.setMaximumSize(QtCore.QSize(500, 250))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        undo_baja_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(undo_baja_window)
        self.centralwidget.setObjectName("centralwidget")
        self.undo_main_title = QtWidgets.QLabel(self.centralwidget)
        self.undo_main_title.setGeometry(QtCore.QRect(0, 30, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.undo_main_title.setFont(font)
        self.undo_main_title.setTextFormat(QtCore.Qt.AutoText)
        self.undo_main_title.setAlignment(QtCore.Qt.AlignCenter)
        self.undo_main_title.setObjectName("undo_main_title")
        self.idempleado_label = QtWidgets.QLabel(self.centralwidget)
        self.idempleado_label.setGeometry(QtCore.QRect(30, 100, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.idempleado_label.setFont(font)
        self.idempleado_label.setObjectName("idempleado_label")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(180, 160, 151, 31))
        self.save_button.setAutoDefault(False)
        self.save_button.setDefault(False)
        self.save_button.setObjectName("save_button")
        self.id_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.id_entry.setGeometry(QtCore.QRect(310, 100, 141, 20))
        self.id_entry.setMaxLength(3)
        self.id_entry.setClearButtonEnabled(True)
        self.id_entry.setObjectName("id_entry")
        undo_baja_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(undo_baja_window)
        QtCore.QMetaObject.connectSlotsByName(undo_baja_window)

        #------------------------------Regex--------------------------------
        self.rx1 = QRegExp("[0-9]+")
        self.id_entry.setValidator(QRegExpValidator(self.rx1))
        #------------------------------End Regex----------------------------

        #------------------------------Events-------------------------------
        self.x = self.save_button.clicked.connect(lambda:self.undo_empleado_controller.deshacer_empleado(self.id_entry.displayText()))
        self.x = self.save_button.clicked.connect(lambda:self.msg_undo_ok())
        self.x = self.save_button.clicked.connect(lambda:self.clear_entrys())
        #----------------------------End Events-----------------------------

    def retranslateUi(self, undo_baja_window):
        _translate = QtCore.QCoreApplication.translate
        undo_baja_window.setWindowTitle(_translate("undo_baja_window", "BD Empleados v2.0"))
        self.undo_main_title.setText(_translate("undo_baja_window", "Complete el siguiente campo:"))
        self.idempleado_label.setText(_translate("undo_baja_window", "Ingrese el ID del empleado:"))
        self.save_button.setText(_translate("undo_baja_window", "Deshacer baja"))

    def msg_undo_ok(self):
        self.msg_upd = QMessageBox()
        self.msg_upd.setIcon(QMessageBox.Information)
        self.msg_upd.setWindowTitle("Deshacer baja")
        self.msg_upd.setText("Se deshizo la baja del ID correctamente!")
        self.msg_upd.setInformativeText("Presione OK para continuar.")
        self.msg_upd.show()

    def clear_entrys(self):
        self.id_entry.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    undo_baja_window = QtWidgets.QMainWindow()
    ui = Ui_undo_baja_window()
    ui.setupUi(undo_baja_window)
    undo_baja_window.show()
    sys.exit(app.exec_())
