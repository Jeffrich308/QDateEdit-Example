# -------------------------------------------------------------------------------
# Name:             DatePicker.py
# Purpose:          Example of the use of DateEdit method
#
# Author:           Jeffreaux
#
# Created:          02July24
#
# Required Packages:    PyQt5, PyQt5-Tools, enable the popup option in Designer
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QLabel, QDateEdit
from PyQt5 import uic
import sys
from datetime import date


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("DatePicker_GUI.ui", self)

        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")
        self.actExit = self.findChild(QAction, "actExit")
        self.dateEdit = self.findChild(QDateEdit, "dateEdit")
        self.label = self.findChild(QLabel, "label")
        self.btnDate = self.findChild(QPushButton, "btnDate")


        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)
        self.actExit.triggered.connect(self.closeEvent)
        self.btnDate.clicked.connect(self.get_date)

        # Set QDateEdit box to today's date
        self.dateEdit.setDate(date.today()) 
        # print(date.today())

        # Show the app
        self.show()


    def get_date(self):
        # .date retrieves the date in the box, toString converts it to a string for proper display
        print(self.dateEdit.date().toString("MM-dd-yyyy"))
        self.label.setText(self.dateEdit.date().toString("MM-dd-yyyy"))

    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
