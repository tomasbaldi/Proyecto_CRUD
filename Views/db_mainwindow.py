import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.db_mainwindow_controller import db_mainwindow_controller


class Ui_main_bd_window(object):

    def __init__(self):
        self.mainwindow_controller = db_mainwindow_controller(self)

    def setupUi(self, main_bd_window):
        main_bd_window.setObjectName("main_bd_window")
        main_bd_window.resize(1000, 550)
        main_bd_window.setMinimumSize(QtCore.QSize(1000, 550))
        main_bd_window.setMaximumSize(QtCore.QSize(1000, 550))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        main_bd_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(main_bd_window)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs_empleados = QtWidgets.QTabWidget(self.centralwidget)
        self.tabs_empleados.setGeometry(QtCore.QRect(2, 10, 761, 491))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(11)
        self.tabs_empleados.setFont(font)
        self.tabs_empleados.setObjectName("tabs_empleados")
        self.activos_empleados = QtWidgets.QWidget()
        self.activos_empleados.setObjectName("activos_empleados")
        self.label_empleados_activos = QtWidgets.QLabel(self.activos_empleados)
        self.label_empleados_activos.setGeometry(QtCore.QRect(10, 30, 731, 21))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(8)
        self.label_empleados_activos.setFont(font)
        self.label_empleados_activos.setAlignment(QtCore.Qt.AlignCenter)
        self.label_empleados_activos.setObjectName("label_empleados_activos")
        self.tabla_empleados_activos = QtWidgets.QTableWidget(self.activos_empleados)
        self.tabla_empleados_activos.setGeometry(QtCore.QRect(10, 70, 731, 381))
        self.tabla_empleados_activos.setTabletTracking(False)
        self.tabla_empleados_activos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_empleados_activos.setTabKeyNavigation(False)
        self.tabla_empleados_activos.setProperty("showDropIndicator", False)
        self.tabla_empleados_activos.setDragDropOverwriteMode(False)
        self.tabla_empleados_activos.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tabla_empleados_activos.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_empleados_activos.setColumnCount(6)
        self.tabla_empleados_activos.setObjectName("tabla_empleados_activos")
        self.tabla_empleados_activos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados_activos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados_activos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados_activos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados_activos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados_activos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados_activos.setHorizontalHeaderItem(5, item)
        self.tabla_empleados_activos.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_empleados_activos.horizontalHeader().setDefaultSectionSize(118)
        self.tabla_empleados_activos.horizontalHeader().setSortIndicatorShown(False)
        self.tabla_empleados_activos.horizontalHeader().setStretchLastSection(True)
        self.tabla_empleados_activos.verticalHeader().setStretchLastSection(False)
        self.tabs_empleados.addTab(self.activos_empleados, "")
        self.inactivos_empleados = QtWidgets.QWidget()
        self.inactivos_empleados.setObjectName("inactivos_empleados")
        self.label_empleados_inactivos = QtWidgets.QLabel(self.inactivos_empleados)
        self.label_empleados_inactivos.setGeometry(QtCore.QRect(10, 30, 731, 21))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(8)
        self.label_empleados_inactivos.setFont(font)
        self.label_empleados_inactivos.setAlignment(QtCore.Qt.AlignCenter)
        self.label_empleados_inactivos.setObjectName("label_empleados_inactivos")
        self.tabla_empleados_inactivos = QtWidgets.QTableWidget(self.inactivos_empleados)
        self.tabla_empleados_inactivos.setGeometry(QtCore.QRect(10, 80, 731, 371))
        self.tabla_empleados_inactivos.setTabletTracking(False)
        self.tabla_empleados_inactivos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tabla_empleados_inactivos.setTabKeyNavigation(False)
        self.tabla_empleados_inactivos.setProperty("showDropIndicator", False)
        self.tabla_empleados_inactivos.setDragDropOverwriteMode(False)
        self.tabla_empleados_inactivos.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tabla_empleados_inactivos.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tabla_empleados_inactivos.setColumnCount(6)
        self.tabla_empleados_inactivos.setObjectName("tabla_empleados_inactivos")
        self.tabla_empleados_inactivos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados_inactivos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados_inactivos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados_inactivos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados_inactivos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados_inactivos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_empleados_inactivos.setHorizontalHeaderItem(5, item)
        self.tabla_empleados_inactivos.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_empleados_inactivos.horizontalHeader().setDefaultSectionSize(118)
        self.tabla_empleados_inactivos.horizontalHeader().setSortIndicatorShown(False)
        self.tabla_empleados_inactivos.horizontalHeader().setStretchLastSection(True)
        self.tabla_empleados_inactivos.verticalHeader().setStretchLastSection(False)
        self.undo_baja_registro = QtWidgets.QPushButton(self.inactivos_empleados)
        self.undo_baja_registro.setGeometry(QtCore.QRect(580, 10, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.undo_baja_registro.setFont(font)
        self.undo_baja_registro.setAutoDefault(False)
        self.undo_baja_registro.setObjectName("undo_baja_registro")
        self.delete_registro = QtWidgets.QPushButton(self.inactivos_empleados)
        self.delete_registro.setGeometry(QtCore.QRect(580, 40, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.delete_registro.setFont(font)
        self.delete_registro.setAutoDefault(False)
        self.delete_registro.setObjectName("delete_registro")
        self.tabs_empleados.addTab(self.inactivos_empleados, "")
        self.agregar_registro = QtWidgets.QPushButton(self.centralwidget)
        self.agregar_registro.setGeometry(QtCore.QRect(800, 120, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.agregar_registro.setFont(font)
        self.agregar_registro.setAutoDefault(True)
        self.agregar_registro.setObjectName("agregar_registro")
        self.modificar_registro = QtWidgets.QPushButton(self.centralwidget)
        self.modificar_registro.setGeometry(QtCore.QRect(800, 190, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.modificar_registro.setFont(font)
        self.modificar_registro.setAutoDefault(True)
        self.modificar_registro.setObjectName("modificar_registro")
        self.baja_registro = QtWidgets.QPushButton(self.centralwidget)
        self.baja_registro.setGeometry(QtCore.QRect(800, 260, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.baja_registro.setFont(font)
        self.baja_registro.setAutoDefault(True)
        self.baja_registro.setObjectName("baja_registro")
        self.consultar_registro = QtWidgets.QPushButton(self.centralwidget)
        self.consultar_registro.setGeometry(QtCore.QRect(800, 330, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.consultar_registro.setFont(font)
        self.consultar_registro.setAutoDefault(True)
        self.consultar_registro.setObjectName("consultar_registro")
        self.refresh_bd_registro = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_bd_registro.setGeometry(QtCore.QRect(780, 400, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.refresh_bd_registro.setFont(font)
        self.refresh_bd_registro.setAutoDefault(True)
        self.refresh_bd_registro.setObjectName("refresh_bd_registro")
        main_bd_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_bd_window)
        self.tabs_empleados.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_bd_window)

    def retranslateUi(self, main_bd_window):
        _translate = QtCore.QCoreApplication.translate
        main_bd_window.setWindowTitle(_translate("main_bd_window", "BD Empleados v2.0"))
        self.label_empleados_activos.setText(_translate("main_bd_window", "Empleados - Activos"))
        item = self.tabla_empleados_activos.horizontalHeaderItem(0)
        item.setText(_translate("main_bd_window", "ID"))
        item = self.tabla_empleados_activos.horizontalHeaderItem(1)
        item.setText(_translate("main_bd_window", "Nombre"))
        item = self.tabla_empleados_activos.horizontalHeaderItem(2)
        item.setText(_translate("main_bd_window", "Apellido"))
        item = self.tabla_empleados_activos.horizontalHeaderItem(3)
        item.setText(_translate("main_bd_window", "Departamento"))
        item = self.tabla_empleados_activos.horizontalHeaderItem(4)
        item.setText(_translate("main_bd_window", "Alta de Empleado"))
        item = self.tabla_empleados_activos.horizontalHeaderItem(5)
        item.setText(_translate("main_bd_window", "Sueldo Bruto"))
        self.tabs_empleados.setTabText(self.tabs_empleados.indexOf(self.activos_empleados), _translate("main_bd_window", "Activos"))
        self.label_empleados_inactivos.setText(_translate("main_bd_window", "Empleados - Inactivos"))
        item = self.tabla_empleados_inactivos.horizontalHeaderItem(0)
        item.setText(_translate("main_bd_window", "ID"))
        item = self.tabla_empleados_inactivos.horizontalHeaderItem(1)
        item.setText(_translate("main_bd_window", "Nombre"))
        item = self.tabla_empleados_inactivos.horizontalHeaderItem(2)
        item.setText(_translate("main_bd_window", "Apellido"))
        item = self.tabla_empleados_inactivos.horizontalHeaderItem(3)
        item.setText(_translate("main_bd_window", "Departamento"))
        item = self.tabla_empleados_inactivos.horizontalHeaderItem(4)
        item.setText(_translate("main_bd_window", "Alta de Empleado"))
        item = self.tabla_empleados_inactivos.horizontalHeaderItem(5)
        item.setText(_translate("main_bd_window", "Baja de Empleado"))
        self.undo_baja_registro.setText(_translate("main_bd_window", "Deshacer baja"))
        self.delete_registro.setText(_translate("main_bd_window", "Eliminar registro"))
        self.tabs_empleados.setTabText(self.tabs_empleados.indexOf(self.inactivos_empleados), _translate("main_bd_window", "Inactivos"))
        self.agregar_registro.setText(_translate("main_bd_window", "Agregar "))
        self.modificar_registro.setText(_translate("main_bd_window", "Modificar"))
        self.baja_registro.setText(_translate("main_bd_window", "Dar de baja"))
        self.consultar_registro.setText(_translate("main_bd_window", "Consultar"))
        self.refresh_bd_registro.setText(_translate("main_bd_window", "Refrescar BD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_bd_window = QtWidgets.QMainWindow()
    ui = Ui_main_bd_window()
    ui.setupUi(main_bd_window)
    main_bd_window.show()
    sys.exit(app.exec_())
