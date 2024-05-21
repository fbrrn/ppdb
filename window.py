import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sqlite3
con = sqlite3.connect('ppdb.db')
cur = con.cursor()

class windowAdmin(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Admin Sekolah")
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
        self.setStyleSheet("#widget_4 QPushButton {\n"
"    border: None;\n"
"}")
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.admin = QtWidgets.QWidget(self.widget)
        self.admin.setObjectName("admin")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.admin)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        
        self.label_2 = QtWidgets.QLabel(self.admin)
        self.label_2.setMinimumSize(QtCore.QSize(100, 30))
        self.label_2.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.admin, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(113, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        
        # Judul NAMA SEKOLAH
        self.nama_sekolah = QtWidgets.QLabel(self.widget_4)
        self.nama_sekolah.setMinimumSize(QtCore.QSize(500, 50))
        self.nama_sekolah.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.nama_sekolah.setFont(font)
        self.nama_sekolah.setAlignment(QtCore.Qt.AlignCenter)
        self.nama_sekolah.setObjectName("nama_sekolah")
        self.horizontalLayout_3.addWidget(self.nama_sekolah)
        spacerItem3 = QtWidgets.QSpacerItem(113, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        
        # Layout judul
        self.horizontalLayout.addWidget(self.widget_4, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.widget)
        
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        
        # PushButton untuk Tambah Siswa
        self.tmbh_siswa = QtWidgets.QPushButton(self.widget_2)
        self.tmbh_siswa.setMinimumSize(QtCore.QSize(330, 50))
        self.tmbh_siswa.setMaximumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.tmbh_siswa.setFont(font)
        self.tmbh_siswa.setObjectName("tmbh_siswa")
        self.gridLayout.addWidget(self.tmbh_siswa, 0, 0, 1, 1)
        
        # PushButton untuk Semua Siswa
        self.semua_siswa = QtWidgets.QPushButton(self.widget_2)
        self.semua_siswa.setMinimumSize(QtCore.QSize(330, 50))
        self.semua_siswa.setMaximumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.semua_siswa.setFont(font)
        self.semua_siswa.setObjectName("semua_siswa")
        self.gridLayout.addWidget(self.semua_siswa, 0, 1, 1, 1)
        
        # PushButton untuk Input Hasil Seleksi
        self.siswa_diterima = QtWidgets.QPushButton(self.widget_2)
        self.siswa_diterima.setMinimumSize(QtCore.QSize(330, 50))
        self.siswa_diterima.setMaximumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.siswa_diterima.setFont(font)
        self.siswa_diterima.setObjectName("siswa_diterima")
        self.gridLayout.addWidget(self.siswa_diterima, 1, 0, 1, 1)
        
        # PushButton untuk Hasil Seleksi
        self.siswa_ditolak = QtWidgets.QPushButton(self.widget_2)
        self.siswa_ditolak.setMinimumSize(QtCore.QSize(330, 50))
        self.siswa_ditolak.setMaximumSize(QtCore.QSize(330, 50))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.siswa_ditolak.setFont(font)
        self.siswa_ditolak.setObjectName("siswa_ditolak")
        self.gridLayout.addWidget(self.siswa_ditolak, 1, 1, 1, 1)
        
        # PushButton untuk Keluar
        self.siswa_diterima_2 = QtWidgets.QPushButton(self.widget_2)
        self.siswa_diterima_2.setMinimumSize(QtCore.QSize(100, 35))
        self.siswa_diterima_2.setMaximumSize(QtCore.QSize(100, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.siswa_diterima_2.setFont(font)
        self.siswa_diterima_2.setObjectName("siswa_diterima_2")
        self.gridLayout.addWidget(self.siswa_diterima_2, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        
        self.tmbh_siswa.clicked.connect(self.tambah_Siswa)
        self.semua_siswa.clicked.connect(self.semua_Siswa)
        self.siswa_diterima.clicked.connect(self.input_Hasil)
        self.siswa_ditolak.clicked.connect(self.hasil_Seleksi)
        
        self.setLayout(self.verticalLayout) 

    def retranslateUi(self):
        self.label_2.setText("ADMIN")
        self.nama_sekolah.setText("SMP Amikom Puwokerto")
        self.tmbh_siswa.setText("TAMBAH SISWA")
        self.semua_siswa.setText("SEMUA SISWA")
        self.siswa_diterima.setText("INPUT HASIL SELEKSI")
        self.siswa_ditolak.setText("DATA HASIL SELEKSI")
        self.siswa_diterima_2.setText("KELUAR")
        self.siswa_diterima_2.clicked.connect(self.baliklogin)
    
    def tambah_Siswa(self):
        from tambahsiswa import tambahSiswa
        self.hide()
        self.addsiswa = tambahSiswa()
        self.addsiswa.show()
            
    def semua_Siswa(self):
        from semuasiswa import semuaSiswa
        self.hide()
        self.semua = semuaSiswa()
        self.semua.show()
        
    def input_Hasil(self):
        from inputhasil import inputHasil
        self.hide()
        self.input = inputHasil()
        self.input.show()

    def hasil_Seleksi(self):
        from hasilseleksi import hasilSeleksi
        self.hide()
        self.hasil = hasilSeleksi()
        self.hasil.show()
        
    def baliklogin(self):
        from login import logIn
        self.close()
        self.out = logIn()
        self.out.show()
    
def main():
    APP = QApplication(sys.argv)
    window = windowAdmin()
    sys.exit(APP.exec())
    
if __name__ == '__main__':
    main()