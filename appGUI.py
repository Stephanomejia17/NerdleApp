from interfaz import gui
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QDialog, QMainWindow
from interfaz import consola
from Clases import Clases
from interfaz.gui import MainWindowNerdle


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindowNerdle()
    win.show()
    sys.exit(app.exec())