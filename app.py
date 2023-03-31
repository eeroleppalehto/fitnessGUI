# MAIN WINDOW FOR FITNESS APPLICATION
# ===================================

# LIBRARIES AND MODULES
import sys  # Needed for starting the application
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import *
from datetime import date

import kuntoilija
import fitness
import timetools

# Class for the main window

class App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        loadUi('app.ui', self)

        self.currentDate = date.today()
        #print(self.currentDate, type(self.currentDate))

        # Elements
        self.nameLE = self.nameLineEdit
        self.birthDE = self.birthDateEdit
        self.heightSB = self.heightDoubleSpinBox
        self.weightSB = self.weightDoubleSpinBox
        self.dateE = self.dateEdit
        self.dateE.setDate(self.currentDate)
        self.sexCB = self.sexComboBox
        self.neckSB = self.neckSpinBox
        self.waistSB = self.waistSpinBox
        self.hipsSB = self.hipsSpinBox

        # Label elements
        self.bmiL = self.bmiLabel
        self.fatFiL = self.fatFiLabel
        self.fatUsL = self.fatUsLabel

        # Button elements
        self.calculatePB = self.calculatePushButton
        self.calculatePB.clicked.connect(self.calculateAll)
        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.calculateAll)

        sexes = ["Mies", "Nainen"]
        self.sexCB.addItems(sexes)

    def calculateAll(self):
        name = self.nameLE.text()
        height = self.heightSB.value()
        weight = self.weightSB.value()
        sex = self.sexCB.currentText()

        neck = float(self.neckSB.value())
        waist = float(self.waistSB.value())
        hips = float(self.hipsSB.value())
        
        # Calculate age from birthday and the day weighing
        birthD = self.birthDE.date()
        weighingD = self.dateE.date()
        age = birthD.daysTo(weighingD) / 365.24

        weighingDText = weighingD.toString(format=Qt.ISODate)
        # print(weighingDText)

        # Create an athlete object
        self.athlete = kuntoilija.Kuntoilija(name, height, weight, age, sex, weighingDText)

        # Calculate fat percent according us armys formulas
        fatFi = self.athlete.rasvaprosentti()
        fatUs = 0

        if sex == 'Mies':
            fatUs = self.athlete.usa_rasvaprosentti_mies(height, waist, neck)
        elif sex == 'Nainen':
            fatUs = self.athlete.usa_rasvaprosentti_nainen(height, waist, hips, neck)
        
        self.bmiL.setText(str(self.athlete.bmi))
        self.fatFiL.setText(str(fatFi))
        self.fatUsL.setText(str(fatUs))

    def saveInfo(self):
        pass


if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    # Create the main window
    appWindow = App()
    appWindow.show()
    sys.exit(app.exec())