import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from window import windowAdmin

import sqlite3
con = sqlite3.connect('ppdb.db')
cur = con.cursor()

class hasilSeleksi(QWidget):
    def __init__(self, parent=None) :
        super().__init__(parent)
        self.setWindowTitle("Input Hasil Seleksi")
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
        self.hasilSeleksi_2425()
        self.hasilSeleksi_2526()
        
    def closeEvent(self, event):
        self.mainwin = windowAdmin()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.back = QtWidgets.QToolButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.horizontalLayout_2.addWidget(self.back)
        self.horizontalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.widget_4, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tahunajaran_tab = QtWidgets.QTabWidget(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tahunajaran_tab.setFont(font)
        self.tahunajaran_tab.setObjectName("tahunajaran_tab")
        self.tab_2425 = QtWidgets.QWidget()
        self.tab_2425.setObjectName("tab_2425")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2425)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tbl2425 = QtWidgets.QTableWidget(self.tab_2425)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tbl2425.setFont(font)
        self.tbl2425.setObjectName("tbl2425")
        self.tbl2425.setColumnCount(4)
        self.tbl2425.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.tbl2425, 1, 0, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.tab_2425)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_3 = QtWidgets.QLabel(self.widget_6)
        self.label_3.setObjectName("label_3")
        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)
        self.cariEdit_2425 = QtWidgets.QLineEdit(self.widget_6)
        self.cariEdit_2425.setObjectName("cariEdit_2425")
        self.gridLayout_7.addWidget(self.cariEdit_2425, 0, 1, 1, 1)
        self.cariBtn_2425 = QtWidgets.QPushButton(self.widget_6)
        self.cariBtn_2425.setObjectName("cariBtn_2425")
        self.gridLayout_7.addWidget(self.cariBtn_2425, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget_6, 0, 0, 1, 1)
        self.tahunajaran_tab.addTab(self.tab_2425, "")
        self.tab_2526 = QtWidgets.QWidget()
        self.tab_2526.setObjectName("tab_2526")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2526)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tbl2526 = QtWidgets.QTableWidget(self.tab_2526)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tbl2526.setFont(font)
        self.tbl2526.setObjectName("tbl2526")
        self.tbl2526.setColumnCount(4)
        self.tbl2526.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(3, item)
        self.gridLayout_3.addWidget(self.tbl2526, 1, 0, 1, 1)
        self.widget_7 = QtWidgets.QWidget(self.tab_2526)
        self.widget_7.setObjectName("widget_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_4 = QtWidgets.QLabel(self.widget_7)
        self.label_4.setObjectName("label_4")
        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)
        self.cariEdit_2526 = QtWidgets.QLineEdit(self.widget_7)
        self.cariEdit_2526.setObjectName("cariEdit_2526")
        self.gridLayout_8.addWidget(self.cariEdit_2526, 0, 1, 1, 1)
        self.cariBtn_2526 = QtWidgets.QPushButton(self.widget_7)
        self.cariBtn_2526.setObjectName("cariBtn_2526")
        self.gridLayout_8.addWidget(self.cariBtn_2526, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.widget_7, 0, 0, 1, 1)
        self.tahunajaran_tab.addTab(self.tab_2526, "")
        self.horizontalLayout_11.addWidget(self.tahunajaran_tab)
        self.verticalLayout.addWidget(self.widget)
        self.tahunajaran_tab.setCurrentIndex(0)

        self.setLayout(self.verticalLayout)

    def retranslateUi(self):
        self.back.setText("KEMBALI")
        self.back.clicked.connect(self.kembali)
        
        self.label.setText("DATA HASIL SELEKSI SISWA")
        self.tbl2425.setSortingEnabled(True)
        item = self.tbl2425.horizontalHeaderItem(0)
        item.setText("No Pendaftaran")
        item = self.tbl2425.horizontalHeaderItem(1)
        item.setText("Nama Lengkap")
        item = self.tbl2425.horizontalHeaderItem(2)
        item.setText("NISN")
        item = self.tbl2425.horizontalHeaderItem(3)
        item.setText("Keterangan")
        self.label_3.setText("Pencarian")
        self.cariBtn_2425.setText("Cari")
        self.cariBtn_2425.clicked.connect(self.search_data_2425)
        self.tahunajaran_tab.setTabText(self.tahunajaran_tab.indexOf(self.tab_2425), "2024/2025")
        
        self.tbl2526.setSortingEnabled(True)
        item = self.tbl2526.horizontalHeaderItem(0)
        item.setText("No Pendaftaran")
        item = self.tbl2526.horizontalHeaderItem(1)
        item.setText("Nama Lengkap")
        item = self.tbl2526.horizontalHeaderItem(2)
        item.setText("NISN")
        item = self.tbl2526.horizontalHeaderItem(3)
        item.setText("Keterangan")
        self.label_4.setText("Pencarian")
        self.cariBtn_2526.setText("Cari")
        self.cariBtn_2526.clicked.connect(self.search_data_2526)
        self.tahunajaran_tab.setTabText(self.tahunajaran_tab.indexOf(self.tab_2526), "2025/2026")
                
    def hasilSeleksi_2425(self):
        con = sqlite3.connect('ppdb.db')
        cur = con.cursor()
        
        query = "SELECT tb_th2425.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_th2425.keterangan FROM tb_th2425 INNER JOIN tb_addsiswa ON tb_th2425.no_daftar = tb_addsiswa.no_daftar ORDER BY tb_th2425.no_daftar DESC;"
        cur.execute(query)
        data_siswa = cur.fetchall()
        
        # menampilkan data siswa pada tabel yang terdapat pada form
        self.tbl2425.setRowCount(len(data_siswa))
        baris = 0
        
        for x in data_siswa:
            self.tbl2425.setItem(baris, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.tbl2425.setItem(baris, 1, QtWidgets.QTableWidgetItem(x[1]))
            self.tbl2425.setItem(baris, 2, QtWidgets.QTableWidgetItem(str(x[2])))
            self.tbl2425.setItem(baris, 3, QtWidgets.QTableWidgetItem(x[3]))
            baris = baris + 1
        # Menyesuaikan lebar kolom dengan panjang karakter data
        self.tbl2425.resizeColumnsToContents()
        
    def hasilSeleksi_2526(self):
        con = sqlite3.connect('ppdb.db')
        cur = con.cursor()
        
        query = "SELECT tb_th2526.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_th2526.keterangan FROM tb_th2526 INNER JOIN tb_addsiswa ON tb_th2526.no_daftar = tb_addsiswa.no_daftar ORDER BY tb_th2526.no_daftar DESC;"
        cur.execute(query)
        data_siswa = cur.fetchall()
        
        # menampilkan data siswa pada tabel yang terdapat pada form
        self.tbl2526.setRowCount(len(data_siswa))
        baris = 0
        
        for x in data_siswa:
            self.tbl2526.setItem(baris, 0, QtWidgets.QTableWidgetItem(str(x[0])))
            self.tbl2526.setItem(baris, 1, QtWidgets.QTableWidgetItem(x[1]))
            self.tbl2526.setItem(baris, 2, QtWidgets.QTableWidgetItem(str(x[2])))
            self.tbl2526.setItem(baris, 3, QtWidgets.QTableWidgetItem(x[3]))
            baris = baris + 1
        # Menyesuaikan lebar kolom dengan panjang karakter data
        self.tbl2526.resizeColumnsToContents()
                
    def search_data_2425(self):
        keyword = "%" + self.cariEdit_2425.text() + "%"
        query = "SELECT tb_th2425.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_th2425.keterangan FROM tb_th2425 INNER JOIN tb_addsiswa ON tb_th2425.no_daftar = tb_addsiswa.no_daftar;"
        parameter = []

        if keyword:
            query = "SELECT tb_th2425.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_th2425.keterangan FROM tb_th2425 INNER JOIN tb_addsiswa ON tb_th2425.no_daftar = tb_addsiswa.no_daftar WHERE LOWER(tb_th2425.no_daftar) LIKE LOWER(?) OR LOWER(tb_addsiswa.nama_lengkap) LIKE LOWER(?) OR LOWER(tb_addsiswa.nisn_siswa) LIKE LOWER(?) OR LOWER(tb_th2425.keterangan) LIKE LOWER(?);"
            parameter = [keyword] * 4

        cur.execute(query, parameter)
        data_input = cur.fetchall()

        tab_count = self.tahunajaran_tab.count()

        for i in range(tab_count):
            table_widget = self.tahunajaran_tab.widget(i).findChild(QtWidgets.QTableWidget)

            table_widget.setRowCount(len(data_input))
            baris = 0

            for x in data_input:
                table_widget.setItem(baris, 0, QtWidgets.QTableWidgetItem(str(x[0])))
                table_widget.setItem(baris, 1, QtWidgets.QTableWidgetItem(x[1]))
                table_widget.setItem(baris, 2, QtWidgets.QTableWidgetItem(str(x[2])))
                table_widget.setItem(baris, 3, QtWidgets.QTableWidgetItem(x[3]))
                baris = baris + 1

            table_widget.resizeColumnsToContents()

    def search_data_2526(self):
        keyword = "%" + self.cariEdit_2526.text() + "%"
        query = "SELECT tb_th2526.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_th2526.keterangan FROM tb_th2526 INNER JOIN tb_addsiswa ON tb_th2526.no_daftar = tb_addsiswa.no_daftar;"
        parameter = []

        if keyword:
            query = "SELECT tb_th2526.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_th2526.keterangan FROM tb_th2526 INNER JOIN tb_addsiswa ON tb_th2526.no_daftar = tb_addsiswa.no_daftar WHERE LOWER(tb_th2526.no_daftar) LIKE LOWER(?) OR LOWER(tb_addsiswa.nama_lengkap) LIKE LOWER(?) OR LOWER(tb_addsiswa.nisn_siswa) LIKE LOWER(?) OR LOWER(tb_th2526.keterangan) LIKE LOWER(?);"
            parameter = [keyword] * 4

        cur.execute(query, parameter)
        data_input = cur.fetchall()

        tab_count = self.tahunajaran_tab.count()

        for i in range(tab_count):
            table_widget = self.tahunajaran_tab.widget(i).findChild(QtWidgets.QTableWidget)

            table_widget.setRowCount(len(data_input))
            baris = 0

            for x in data_input:
                table_widget.setItem(baris, 0, QtWidgets.QTableWidgetItem(str(x[0])))
                table_widget.setItem(baris, 1, QtWidgets.QTableWidgetItem(x[1]))
                table_widget.setItem(baris, 2, QtWidgets.QTableWidgetItem(str(x[2])))
                table_widget.setItem(baris, 3, QtWidgets.QTableWidgetItem(x[3]))
                baris = baris + 1

            table_widget.resizeColumnsToContents()
        
    def kembali(self):
        self.close()
        
def main():
    APP = QApplication(sys.argv)
    window = hasilSeleksi()
    sys.exit(APP.exec())

if __name__ == '__main__':
    main()
