# main.py
from PyQt5.QtWidgets import QApplication
from gui.mainwindow import MainAppWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainAppWindow()
    main_window.show()
    sys.exit(app.exec_())

