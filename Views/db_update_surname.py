import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_update_apellido_window(object):
    def setupUi(self, update_apellido_window):
        update_apellido_window.setObjectName("update_apellido_window")
        update_apellido_window.resize(500, 300)
        update_apellido_window.setMinimumSize(QtCore.QSize(500, 300))
        update_apellido_window.setMaximumSize(QtCore.QSize(500, 300))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        update_apellido_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(update_apellido_window)
        self.centralwidget.setObjectName("centralwidget")
        self.upd_surname_maintitle = QtWidgets.QLabel(self.centralwidget)
        self.upd_surname_maintitle.setGeometry(QtCore.QRect(0, 30, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.upd_surname_maintitle.setFont(font)
        self.upd_surname_maintitle.setTextFormat(QtCore.Qt.AutoText)
        self.upd_surname_maintitle.setAlignment(QtCore.Qt.AlignCenter)
        self.upd_surname_maintitle.setObjectName("upd_surname_maintitle")
        self.idempleado_label = QtWidgets.QLabel(self.centralwidget)
        self.idempleado_label.setGeometry(QtCore.QRect(30, 100, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.idempleado_label.setFont(font)
        self.idempleado_label.setObjectName("idempleado_label")
        self.upd_surname_label = QtWidgets.QLabel(self.centralwidget)
        self.upd_surname_label.setGeometry(QtCore.QRect(30, 140, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.upd_surname_label.setFont(font)
        self.upd_surname_label.setObjectName("upd_surname_label")
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
        self.upd_surname_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.upd_surname_entry.setGeometry(QtCore.QRect(310, 150, 141, 20))
        self.upd_surname_entry.setMaxLength(20)
        self.upd_surname_entry.setClearButtonEnabled(True)
        self.upd_surname_entry.setObjectName("upd_surname_entry")
        update_apellido_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(update_apellido_window)
        QtCore.QMetaObject.connectSlotsByName(update_apellido_window)

    def retranslateUi(self, update_apellido_window):
        _translate = QtCore.QCoreApplication.translate
        update_apellido_window.setWindowTitle(_translate("update_apellido_window", "BD Empleados v2.0"))
        self.upd_surname_maintitle.setText(_translate("update_apellido_window", "Complete los siguientes campos:"))
        self.idempleado_label.setText(_translate("update_apellido_window", "Ingrese el ID del empleado:"))
        self.upd_surname_label.setText(_translate("update_apellido_window", "<html><head/><body><p>Ingrese un nuevo apellido<br/>para el ID ingresado:</p></body></html>"))
        self.save_button.setText(_translate("update_apellido_window", "Aplicar cambios"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    update_apellido_window = QtWidgets.QMainWindow()
    ui = Ui_update_apellido_window()
    ui.setupUi(update_apellido_window)
    update_apellido_window.show()
    sys.exit(app.exec_())
