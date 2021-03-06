import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.db_search_controller import db_search_controller
from Views.db_searchresults import Ui_searchresults_window
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator

class Ui_search_window(object):

    def __init__(self):
        self.search_controller = db_search_controller(self)

    def setupUi(self, search_window):
        search_window.setObjectName("search_window")
        search_window.resize(600, 400)
        search_window.setMinimumSize(QtCore.QSize(600, 400))
        search_window.setMaximumSize(QtCore.QSize(600, 500))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(12)
        search_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(search_window)
        self.centralwidget.setObjectName("centralwidget")
        self.search_main_title = QtWidgets.QLabel(self.centralwidget)
        self.search_main_title.setGeometry(QtCore.QRect(0, 30, 601, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.search_main_title.setFont(font)
        self.search_main_title.setTextFormat(QtCore.Qt.AutoText)
        self.search_main_title.setAlignment(QtCore.Qt.AlignCenter)
        self.search_main_title.setObjectName("search_main_title")
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
        self.date_label.setGeometry(QtCore.QRect(40, 210, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.sueldo_label = QtWidgets.QLabel(self.centralwidget)
        self.sueldo_label.setGeometry(QtCore.QRect(40, 250, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.sueldo_label.setFont(font)
        self.sueldo_label.setObjectName("sueldo_label")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(220, 310, 171, 31))
        self.search_button.setAutoDefault(False)
        self.search_button.setDefault(False)
        self.search_button.setObjectName("search_button")
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
        self.entry_alta_date_min = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_alta_date_min.setGeometry(QtCore.QRect(230, 210, 121, 20))
        self.entry_alta_date_min.setMaxLength(10)
        self.entry_alta_date_min.setClearButtonEnabled(True)
        self.entry_alta_date_min.setObjectName("entry_alta_date_min")
        self.entry_alta_date_max = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_alta_date_max.setGeometry(QtCore.QRect(400, 210, 121, 20))
        self.entry_alta_date_max.setMaxLength(10)
        self.entry_alta_date_max.setClearButtonEnabled(True)
        self.entry_alta_date_max.setObjectName("entry_alta_date_max")
        self.betweendate_label = QtWidgets.QLabel(self.centralwidget)
        self.betweendate_label.setGeometry(QtCore.QRect(370, 210, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.betweendate_label.setFont(font)
        self.betweendate_label.setObjectName("betweendate_label")
        self.entry_salary_min = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_salary_min.setGeometry(QtCore.QRect(230, 250, 121, 20))
        self.entry_salary_min.setMaxLength(10)
        self.entry_salary_min.setClearButtonEnabled(True)
        self.entry_salary_min.setObjectName("entry_salary_min")
        self.betweensalary_label = QtWidgets.QLabel(self.centralwidget)
        self.betweensalary_label.setGeometry(QtCore.QRect(370, 250, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.betweensalary_label.setFont(font)
        self.betweensalary_label.setObjectName("betweensalary_label")
        self.entry_salary_max = QtWidgets.QLineEdit(self.centralwidget)
        self.entry_salary_max.setGeometry(QtCore.QRect(400, 250, 121, 20))
        self.entry_salary_max.setMaxLength(10)
        self.entry_salary_max.setClearButtonEnabled(True)
        self.entry_salary_max.setObjectName("entry_salary_max")
        search_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(search_window)
        QtCore.QMetaObject.connectSlotsByName(search_window)

        #------------------------------Regex--------------------------------
        self.rx1 = QRegExp("[a-z ]+")
        self.entry_alta_nombre.setValidator(QRegExpValidator(self.rx1))
        self.rx2 = QRegExp("[a-z ]+")
        self.entry_alta_apellido.setValidator(QRegExpValidator(self.rx2))
        self.rx3 = QRegExp("[a-z ]+")
        self.entry_alta_depto.setValidator(QRegExpValidator(self.rx3))
        self.rx4 = QRegExp("[0-9]+")
        self.entry_alta_date_min.setValidator(QRegExpValidator(self.rx4))
        self.entry_alta_date_min.setInputMask("9999-99-99")
        self.rx5 = QRegExp("[0-9]+")
        self.entry_alta_date_max.setValidator(QRegExpValidator(self.rx5))
        self.entry_alta_date_max.setInputMask("9999-99-99")
        self.rx6 = QRegExp("[0-9]+")
        self.entry_salary_min.setValidator(QRegExpValidator(self.rx6))
        self.rx7 = QRegExp("[0-9]+")
        self.entry_salary_max.setValidator(QRegExpValidator(self.rx7))
        #------------------------------End Regex----------------------------        
        
        #------------------------------Events-------------------------------    
        self.x = self.search_button.clicked.connect(lambda:self.buscar_datos(self.entry_alta_nombre.text(), self.entry_alta_apellido.text(), self.entry_alta_depto.text(), self.entry_alta_date_min.text(), self.entry_alta_date_max.text(), self.entry_salary_min.text(), self.entry_salary_max.text()))
        
        self.x = self.search_button.clicked.connect(lambda:self.clear_entrys())
        #----------------------------End Events-----------------------------
    
    def buscar_datos(self, str_nombre, str_apellido, str_departamento, str_alta_de_empleado_min, str_alta_de_empleado_max, str_sueldo_bruto_min, str_sueldo_bruto_max):
        datos_encontrados = self.search_controller.buscar(str_nombre, str_apellido, str_departamento, str_alta_de_empleado_min, str_alta_de_empleado_max, str_sueldo_bruto_min, str_sueldo_bruto_max)
        self.search_controller.resultados(self, Ui_searchresults_window, datos_encontrados)
    
    def retranslateUi(self, search_window):
        _translate = QtCore.QCoreApplication.translate
        search_window.setWindowTitle(_translate("search_window", "BD Empleados v2.0"))
        self.search_main_title.setText(_translate("search_window", "Ingrese los criterios de búsqueda a continuación:"))
        self.nombre_label.setText(_translate("search_window", "Nombre:"))
        self.apellido_label.setText(_translate("search_window", "Apellido:"))
        self.depto_label.setText(_translate("search_window", "Departamento:"))
        self.date_label.setText(_translate("search_window", "Fecha de alta entre:"))
        self.sueldo_label.setText(_translate("search_window", "Sueldo Bruto entre:"))
        self.search_button.setText(_translate("search_window", "Buscar"))
        self.betweendate_label.setText(_translate("search_window", "y"))
        self.betweensalary_label.setText(_translate("search_window", "y"))

    def clear_entrys(self):
        self.entry_alta_nombre.clear()
        self.entry_alta_apellido.clear()
        self.entry_alta_depto.clear()
        self.entry_alta_date_min.clear()
        self.entry_alta_date_max.clear()
        self.entry_salary_min.clear()
        self.entry_salary_max.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    search_window = QtWidgets.QMainWindow()
    ui = Ui_search_window()
    ui.setupUi(search_window)
    search_window.show()
    sys.exit(app.exec_())
