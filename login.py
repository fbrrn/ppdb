import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from window import windowAdmin

import sqlite3
con = sqlite3.connect('ppdb.db')
cur = con.cursor()

class logIn(QWidget):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle("Menu Log In")
        self.setGeometry(0, 0, 891, 496)
        cwa = self.frameGeometry()
        cwc = QDesktopWidget().availableGeometry().center()
        cwa.moveCenter(cwc)
        self.move(cwa.topLeft())
        self.UI()
        self.show()
        
    def UI(self):
        self.setupUi()
        self.retranslateUi()
    
    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.widget)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 5, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.widget_2)
        self.statusbar = QtWidgets.QStatusBar()
        self.statusbar.setObjectName("statusbar")
        
        self.setLayout(self.formLayout) 
        
    def retranslateUi(self):
        self.label.setText("SELAMAT DATANG DI APILKASI PPDB")
        self.pushButton_2.setText("Batal")
        self.label_2.setText("NPSN")
        self.label_3.setText("Kata Sandi")
        self.pushButton.setText("Masuk")
    
    def retranslateUi(self):
        self.label.setText("SELAMAT DATANG DI APILKASI PPDB")
        self.label_2.setText("NPSN :")
        self.label_3.setText("Password :")
        
        self.pushButton.setText("Masuk")
        self.pushButton.clicked.connect(self.checkLogin)

        self.pushButton_2.setText("Daftar")
        self.pushButton_2.clicked.connect(self.addSkul)
        
    def addSkul(self):
        from daftar_sekolah import DaftarSekolah
        self.hide()
        self.btnback = DaftarSekolah()
        self.btnback.show()
        
    def checkLogin(self):
        npsn = self.lineEdit.text()
        password = self.lineEdit_2.text()

        cur.execute("SELECT * FROM tb_addskul WHERE npsn=? AND pass=?", (npsn, password))
        user = cur.fetchone()

        if user:
            self.openMainWindow()
        else:
            QMessageBox.warning(self, "Login Gagal", "NPSN atau password salah.")

    def openMainWindow(self):
        self.hide()
        self.mainWindow = windowAdmin()
        self.mainWindow.show()

def main():
    APP = QApplication(sys.argv)
    window = logIn()
    sys.exit(APP.exec())
    
if __name__ == '__main__':
    main()
