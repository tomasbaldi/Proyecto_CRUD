import sys 
import os
myDir = os.getcwd()
sys.path.append(myDir)

from PyQt5 import QtCore, QtGui, QtWidgets
from Controllers.db_searchresults_controller import db_searchresults_controller


class Ui_searchresults_window(object):

    def __init__(self):
        self.searchresults_controller = db_searchresults_controller(self)

    def setupUi(self, searchresults_window):
        searchresults_window.setObjectName("searchresults_window")
        searchresults_window.resize(770, 550)
        searchresults_window.setMinimumSize(QtCore.QSize(770, 550))
        searchresults_window.setMaximumSize(QtCore.QSize(770, 550))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        searchresults_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(searchresults_window)
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.search_empleados_table = QtWidgets.QTableWidget(self.centralwidget)
        self.search_empleados_table.setGeometry(QtCore.QRect(10, 60, 751, 381))
        self.search_empleados_table.setTabletTracking(False)
        self.search_empleados_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.search_empleados_table.setTabKeyNavigation(False)
        self.search_empleados_table.setProperty("showDropIndicator", False)
        self.search_empleados_table.setDragDropOverwriteMode(False)
        self.search_empleados_table.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.search_empleados_table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.search_empleados_table.setColumnCount(6)
        self.search_empleados_table.setObjectName("search_empleados_table")
        self.search_empleados_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.search_empleados_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_empleados_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_empleados_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_empleados_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_empleados_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.search_empleados_table.setHorizontalHeaderItem(5, item)
        self.search_empleados_table.horizontalHeader().setCascadingSectionResizes(False)
        self.search_empleados_table.horizontalHeader().setDefaultSectionSize(118)
        self.search_empleados_table.horizontalHeader().setSortIndicatorShown(False)
        self.search_empleados_table.horizontalHeader().setStretchLastSection(True)
        self.search_empleados_table.verticalHeader().setStretchLastSection(False)
        self.label_empleados_activos = QtWidgets.QLabel(self.centralwidget)
        self.label_empleados_activos.setGeometry(QtCore.QRect(0, 20, 751, 21))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(8)
        self.label_empleados_activos.setFont(font)
        self.label_empleados_activos.setAlignment(QtCore.Qt.AlignCenter)
        self.label_empleados_activos.setObjectName("label_empleados_activos")
        self.search_again_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_again_button.setGeometry(QtCore.QRect(280, 472, 181, 41))
        self.search_again_button.setObjectName("search_again_button")
        searchresults_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(searchresults_window)
        QtCore.QMetaObject.connectSlotsByName(searchresults_window)

        #------------------------------Events-------------------------------    
        self.x = self.search_again_button.clicked.connect(lambda:self.searchresults_controller.ocultar_ventana(searchresults_window))
        #----------------------------End Events-----------------------------

    def retranslateUi(self, searchresults_window):
        _translate = QtCore.QCoreApplication.translate
        searchresults_window.setWindowTitle(_translate("searchresults_window", "BD Empleados v2.0"))
        item = self.search_empleados_table.horizontalHeaderItem(0)
        item.setText(_translate("searchresults_window", "ID"))
        item = self.search_empleados_table.horizontalHeaderItem(1)
        item.setText(_translate("searchresults_window", "Nombre"))
        item = self.search_empleados_table.horizontalHeaderItem(2)
        item.setText(_translate("searchresults_window", "Apellido"))
        item = self.search_empleados_table.horizontalHeaderItem(3)
        item.setText(_translate("searchresults_window", "Departamento"))
        item = self.search_empleados_table.horizontalHeaderItem(4)
        item.setText(_translate("searchresults_window", "Alta de Empleado"))
        item = self.search_empleados_table.horizontalHeaderItem(5)
        item.setText(_translate("searchresults_window", "Sueldo Bruto"))
        self.label_empleados_activos.setText(_translate("searchresults_window", "Resultados de búsqueda:"))
        self.search_again_button.setText(_translate("searchresults_window", "Hacer otra consulta"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    searchresults_window = QtWidgets.QMainWindow()
    ui = Ui_searchresults_window()
    ui.setupUi(searchresults_window)
    searchresults_window.show()
    sys.exit(app.exec_())
