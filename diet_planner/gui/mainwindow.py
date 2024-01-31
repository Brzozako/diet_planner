# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtWidgets import QFileDialog
from .meal_plan import MealPlan
from .nutrient_analysis import NutrientAnalysis
from .user_preferences import UserPreferences
from datetime import datetime

class MainAppWindow(QMainWindow):
    def __init__(self):
        super(MainAppWindow, self).__init__()
        self.setupUi(self)
        self.user_preferences = UserPreferences()
        self.initialize_modules()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 91, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 91, 31))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 10, 131, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 60, 131, 31))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 110, 131, 31))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 10, 181, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 80, 181, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 10, 181, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(670, 10, 121, 31))
        self.dateEdit.setObjectName("dateEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Imię: "))
        self.label_2.setText(_translate("MainWindow", "Waga (kg): "))
        self.label_3.setText(_translate("MainWindow", "Plan Diety: "))
        self.pushButton.setText(_translate("MainWindow", "Dodaj Nowego Użytkownika"))
        self.pushButton_2.setText(_translate("MainWindow", "Zapisz Plan Diety"))
        self.pushButton_3.setText(_translate("MainWindow", "Pokaż Statystyki"))

    def initialize_modules(self):
        # Inicjalizacja modułu GUI
        self.pushButton.clicked.connect(self.add_new_user)
        self.pushButton_2.clicked.connect(self.save_diet_plan)
        self.pushButton_3.clicked.connect(self.show_statistics)

    def add_new_user(self):
        name = self.lineEdit.text()
        weight = float(self.lineEdit_2.text())
        diet_plan = self.lineEdit_3.text()


        self.user_preferences.set_goals({'goal1': 2000, 'goal2': 100})
        self.user_preferences.set_user_data({'age': 25, 'gender': 'male', 'activity_level': 'moderate'})
        self.user_preferences.save_user_info(name, weight, diet_plan)


        self.user_preferences.save_to_file()

        QMessageBox.information(self, "Nowy Użytkownik",
                                f"Dodano nowego użytkownika:\n{name}, {weight} kg, Plan: {diet_plan}. Zapisano informacje do pliku.")

    def save_diet_plan(self):
        meal_name = self.lineEdit.text()
        nutrients = {'protein': 30, 'carbs': 50, 'fat': 20}


        current_date = datetime.now().strftime("%Y-%m-%d")


        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_path, _ = file_dialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.txt)')

        if file_path:
            with open(file_path, 'a') as file:
                file.write(f"{current_date} - {meal_name}: {nutrients}\n")

            QMessageBox.information(self, "Zapisano Plan Diety", f"Zapisano plan diety: {meal_name}")

    def show_statistics(self):

        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_path, _ = file_dialog.getOpenFileName(self, 'Open File', '', 'Text Files (*.txt)')
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                QMessageBox.information(self, "Statystyki z pliku", f"Dane z pliku:\n{content}")

        pass

    def run(self):
        app = QApplication([])
        self.show()
        app.exec_()
