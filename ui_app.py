# Form implementation generated from reading ui file 'c:\Users\EL\Documents\GitHub\fitnessGUI\app.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(362, 693)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(31, 51, 24, 16))
        self.nameLabel.setObjectName("nameLabel")
        self.nameLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nameLineEdit.setGeometry(QtCore.QRect(31, 71, 125, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setToolTipDuration(3)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(190, 130, 87, 23))
        self.dateEdit.setObjectName("dateEdit")
        self.heightDoubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.heightDoubleSpinBox.setGeometry(QtCore.QRect(30, 130, 62, 23))
        self.heightDoubleSpinBox.setObjectName("heightDoubleSpinBox")
        self.weightDoubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.weightDoubleSpinBox.setGeometry(QtCore.QRect(110, 130, 62, 23))
        self.weightDoubleSpinBox.setObjectName("weightDoubleSpinBox")
        self.dateLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.dateLabel.setGeometry(QtCore.QRect(190, 110, 68, 16))
        self.dateLabel.setObjectName("dateLabel")
        self.heightLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.heightLabel.setGeometry(QtCore.QRect(30, 110, 50, 14))
        self.heightLabel.setObjectName("heightLabel")
        self.weightLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.weightLabel.setGeometry(QtCore.QRect(110, 110, 50, 14))
        self.weightLabel.setObjectName("weightLabel")
        self.calculatePushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculatePushButton.setGeometry(QtCore.QRect(30, 270, 80, 22))
        self.calculatePushButton.setObjectName("calculatePushButton")
        self.savePushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.savePushButton.setGeometry(QtCore.QRect(120, 270, 80, 22))
        self.savePushButton.setObjectName("savePushButton")
        self.sexComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.sexComboBox.setGeometry(QtCore.QRect(30, 180, 120, 22))
        self.sexComboBox.setObjectName("sexComboBox")
        self.neckSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.neckSpinBox.setGeometry(QtCore.QRect(30, 230, 50, 23))
        self.neckSpinBox.setObjectName("neckSpinBox")
        self.waistSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.waistSpinBox.setGeometry(QtCore.QRect(100, 230, 50, 23))
        self.waistSpinBox.setObjectName("waistSpinBox")
        self.hipsSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.hipsSpinBox.setGeometry(QtCore.QRect(170, 230, 50, 23))
        self.hipsSpinBox.setObjectName("hipsSpinBox")
        self.sexLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.sexLabel.setGeometry(QtCore.QRect(30, 160, 70, 14))
        self.sexLabel.setObjectName("sexLabel")
        self.neckLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.neckLabel.setGeometry(QtCore.QRect(30, 210, 70, 14))
        self.neckLabel.setObjectName("neckLabel")
        self.waistLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.waistLabel.setGeometry(QtCore.QRect(100, 210, 70, 14))
        self.waistLabel.setObjectName("waistLabel")
        self.hipsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.hipsLabel.setGeometry(QtCore.QRect(170, 210, 70, 14))
        self.hipsLabel.setObjectName("hipsLabel")
        self.birthDateLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.birthDateLabel.setGeometry(QtCore.QRect(170, 50, 90, 16))
        self.birthDateLabel.setObjectName("birthDateLabel")
        self.birthDateEdit = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.birthDateEdit.setGeometry(QtCore.QRect(170, 70, 87, 23))
        self.birthDateEdit.setObjectName("birthDateEdit")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 340, 80, 14))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 320, 340, 3))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.bmiLabe = QtWidgets.QLabel(parent=self.centralwidget)
        self.bmiLabe.setGeometry(QtCore.QRect(30, 360, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bmiLabe.setFont(font)
        self.bmiLabe.setObjectName("bmiLabe")
        self.fatFiLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.fatFiLabel.setGeometry(QtCore.QRect(30, 430, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fatFiLabel.setFont(font)
        self.fatFiLabel.setObjectName("fatFiLabel")
        self.bmiLabel_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.bmiLabel_2.setGeometry(QtCore.QRect(30, 410, 100, 14))
        self.bmiLabel_2.setObjectName("bmiLabel_2")
        self.fatUsLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.fatUsLabel.setGeometry(QtCore.QRect(30, 500, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fatUsLabel.setFont(font)
        self.fatUsLabel.setObjectName("fatUsLabel")
        self.bmiLabel_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.bmiLabel_3.setGeometry(QtCore.QRect(30, 480, 110, 14))
        self.bmiLabel_3.setObjectName("bmiLabel_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 362, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nameLabel.setText(_translate("MainWindow", "Nimi"))
        self.nameLineEdit.setToolTip(_translate("MainWindow", "Kirjoita nimesi kenttään"))
        self.nameLineEdit.setPlaceholderText(_translate("MainWindow", "Kirjoita nimesi"))
        self.dateLabel.setText(_translate("MainWindow", "Mittauspäivä"))
        self.heightLabel.setText(_translate("MainWindow", "Pituus"))
        self.weightLabel.setText(_translate("MainWindow", "Paino"))
        self.calculatePushButton.setText(_translate("MainWindow", "Laske"))
        self.savePushButton.setText(_translate("MainWindow", "Tallenna"))
        self.sexComboBox.setPlaceholderText(_translate("MainWindow", "Valitse sukupuoli"))
        self.sexLabel.setText(_translate("MainWindow", "Sukupuoli"))
        self.neckLabel.setText(_translate("MainWindow", "Kaula"))
        self.waistLabel.setText(_translate("MainWindow", "Vyötärö"))
        self.hipsLabel.setText(_translate("MainWindow", "Lantio"))
        self.birthDateLabel.setText(_translate("MainWindow", "Syntymäpäivä"))
        self.label.setText(_translate("MainWindow", "Painoindeksi"))
        self.bmiLabe.setText(_translate("MainWindow", "Painoindeksi"))
        self.fatFiLabel.setText(_translate("MainWindow", "Rasvaprosentti(FI)"))
        self.bmiLabel_2.setText(_translate("MainWindow", "Rasvaprosentti(FI)"))
        self.fatUsLabel.setText(_translate("MainWindow", "Rasvaprosentti(US)"))
        self.bmiLabel_3.setText(_translate("MainWindow", "Rasvaprosentti(US)"))
