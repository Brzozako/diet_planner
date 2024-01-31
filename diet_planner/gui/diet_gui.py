# diet_planner/gui/diet_gui.py
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from .mainwindow import MainAppWindow

class DietGUI(QMainWindow, MainAppWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initialize_modules()



    def run(self):
        app = QApplication([])
        self.show()
        app.exec_()
