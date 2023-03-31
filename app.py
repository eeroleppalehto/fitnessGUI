# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys  # Needed for starting the application
from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtCore import *
from datetime import date



# Class for the main window

class App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        loadUi('app.ui', self)

        self.calculatePB = self.calculatePushButton
        self.calculatePB.clicked.connect(self.calculateAll)

    def calculateAll(self):
        self.bmiLabel.setText('100')



if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    # Create the main window
    appWindow = App()
    appWindow.show()
    sys.exit(app.exec())