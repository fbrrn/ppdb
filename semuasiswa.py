import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sqlite3
con = sqlite3.connect('ppdb.db')
cur = con.cursor()

class semuaSiswa(QWidget):    
    def __init__(self, parent=None) :
        super().__init__(parent)
        self.setWindowTitle("Data Semua Siswa")
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
        self.tampilDataSemuaSiswa2425()
        self.tampilDataSemuaSiswa2526()
        
    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.back = QtWidgets.QToolButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.back.setFont(font)
        self.back.setObjectName("back")
        self.horizontalLayout_2.addWidget(self.back)
        self.horizontalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.widget_4)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tahunajaran_tab = QtWidgets.QTabWidget(self.widget_2)
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
        self.tbl2425.setColumnCount(15)
        self.tbl2425.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2425.setHorizontalHeaderItem(14, item)
        self.gridLayout_2.addWidget(self.tbl2425, 1, 0, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.tab_2425)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout.setObjectName("gridLayout")
        self.cariLbl = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cariLbl.setFont(font)
        self.cariLbl.setObjectName("cariLbl")
        self.gridLayout.addWidget(self.cariLbl, 0, 0, 1, 1)
        self.cariEdit_2425 = QtWidgets.QLineEdit(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cariEdit_2425.setFont(font)
        self.cariEdit_2425.setObjectName("cariEdit_2425")
        self.gridLayout.addWidget(self.cariEdit_2425, 0, 1, 1, 1)
        self.cariBtn_2425 = QtWidgets.QPushButton(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cariBtn_2425.setFont(font)
        self.cariBtn_2425.setObjectName("cariBtn_2425")
        self.gridLayout.addWidget(self.cariBtn_2425, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.widget_5, 0, 0, 1, 1)
        self.hapusBtn_2425 = QtWidgets.QPushButton(self.tab_2425)
        self.hapusBtn_2425.setObjectName("hapusBtn_2425")
        self.gridLayout_2.addWidget(self.hapusBtn_2425, 3, 0, 1, 1)
        self.editBtn_2425 = QtWidgets.QPushButton(self.tab_2425)
        self.editBtn_2425.setObjectName("editBtn_2425")
        self.gridLayout_2.addWidget(self.editBtn_2425, 2, 0, 1, 1)
        self.tahunajaran_tab.addTab(self.tab_2425, "")
        self.tab_2526 = QtWidgets.QWidget()
        self.tab_2526.setObjectName("tab_2526")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2526)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.tab_2526)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)
        self.cariEdit_2526 = QtWidgets.QLineEdit(self.widget_6)
        self.cariEdit_2526.setObjectName("cariEdit_2526")
        self.gridLayout_4.addWidget(self.cariEdit_2526, 0, 1, 1, 1)
        self.cariBtn_2526 = QtWidgets.QPushButton(self.widget_6)
        self.cariBtn_2526.setObjectName("cariBtn_2526")
        self.gridLayout_4.addWidget(self.cariBtn_2526, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.widget_6, 0, 0, 1, 1)
        self.hapusBtn_2526 = QtWidgets.QPushButton(self.tab_2526)
        self.hapusBtn_2526.setObjectName("hapusBtn_2526")
        self.gridLayout_3.addWidget(self.hapusBtn_2526, 3, 0, 1, 1)
        self.tbl2526 = QtWidgets.QTableWidget(self.tab_2526)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tbl2526.setFont(font)
        self.tbl2526.setObjectName("tbl2526")
        self.tbl2526.setColumnCount(15)
        self.tbl2526.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl2526.setHorizontalHeaderItem(14, item)
        self.gridLayout_3.addWidget(self.tbl2526, 1, 0, 1, 1)
        self.editBtn_2526 = QtWidgets.QPushButton(self.tab_2526)
        self.editBtn_2526.setObjectName("editBtn_2526")
        self.gridLayout_3.addWidget(self.editBtn_2526, 2, 0, 1, 1)
        self.tahunajaran_tab.addTab(self.tab_2526, "")
        self.verticalLayout_2.addWidget(self.tahunajaran_tab)
        self.verticalLayout.addWidget(self.widget_2)
        self.tahunajaran_tab.setCurrentIndex(0)

        self.setLayout(self.verticalLayout)

    def retranslateUi(self):
        self.back.setText("KEMBALI")
        self.back.clicked.connect(self.kembali)

        self.label.setText("DATA SEMUA SISWA")
        self.tbl2425.setSortingEnabled(True)
        item = self.tbl2425.horizontalHeaderItem(0)
        item.setText("No Pendaftaran")
        item = self.tbl2425.horizontalHeaderItem(1)
        item.setText("Nama Lengkap")
        item = self.tbl2425.horizontalHeaderItem(2)
        item.setText("NISN Siswa")
        item = self.tbl2425.horizontalHeaderItem(3)
        item.setText("Alamat Siswa")
        item = self.tbl2425.horizontalHeaderItem(4)
        item.setText("Tempat Lahir")
        item = self.tbl2425.horizontalHeaderItem(5)
        item.setText("Tanggal Lahir")
        item = self.tbl2425.horizontalHeaderItem(6)
        item.setText("Jenis Kelamin")
        item = self.tbl2425.horizontalHeaderItem(7)
        item.setText("Agama")
        item = self.tbl2425.horizontalHeaderItem(8)
        item.setText("Asal Sekolah")
        item = self.tbl2425.horizontalHeaderItem(9)
        item.setText("Alamat Sekolah")
        item = self.tbl2425.horizontalHeaderItem(10)
        item.setText("Nama Ayah/Wali")
        item = self.tbl2425.horizontalHeaderItem(11)
        item.setText("Nama Ibu")
        item = self.tbl2425.horizontalHeaderItem(12)
        item.setText("Penghasilan Orang Tua")
        item = self.tbl2425.horizontalHeaderItem(13)
        item.setText("Nomor Telepon/Handphone")
        item = self.tbl2425.horizontalHeaderItem(14)
        item.setText("Tanggal Daftar")
        self.cariLbl.setText("Pencarian")
        self.cariBtn_2425.setText("Cari")
        self.cariBtn_2425.clicked.connect(self.search_data_2425)
        self.hapusBtn_2425.setText("Hapus Data")
        self.hapusBtn_2425.clicked.connect(self.hapus)
        self.editBtn_2425.setText("Edit Data")
        self.editBtn_2425.clicked.connect(self.edit)
        self.tahunajaran_tab.setTabText(self.tahunajaran_tab.indexOf(self.tab_2425), "2024/2025")
        
        self.label_2.setText("Pencarian")
        self.cariBtn_2526.setText("Cari")
        self.cariBtn_2526.clicked.connect(self.search_data_2526)
        self.hapusBtn_2526.setText("Hapus Data")
        self.hapusBtn_2526.clicked.connect(self.hapus2526)
        self.tbl2526.setSortingEnabled(True)
        item = self.tbl2526.horizontalHeaderItem(0)
        item.setText("No Pendaftaran")
        item = self.tbl2526.horizontalHeaderItem(1)
        item.setText("Nama Lengkap")
        item = self.tbl2526.horizontalHeaderItem(2)
        item.setText("NISN Siswa")
        item = self.tbl2526.horizontalHeaderItem(3)
        item.setText("Alamat Siswa")
        item = self.tbl2526.horizontalHeaderItem(4)
        item.setText("Tempat Lahir")
        item = self.tbl2526.horizontalHeaderItem(5)
        item.setText("Tanggal Lahir")
        item = self.tbl2526.horizontalHeaderItem(6)
        item.setText("Jenis Kelamin")
        item = self.tbl2526.horizontalHeaderItem(7)
        item.setText("Agama")
        item = self.tbl2526.horizontalHeaderItem(8)
        item.setText("Asal Sekolah")
        item = self.tbl2526.horizontalHeaderItem(9)
        item.setText("Alamat Sekolah")
        item = self.tbl2526.horizontalHeaderItem(10)
        item.setText("Nama Ayah/Wali")
        item = self.tbl2526.horizontalHeaderItem(11)
        item.setText("Nama Ibu")
        item = self.tbl2526.horizontalHeaderItem(12)
        item.setText("Penghasilan Orang Tua")
        item = self.tbl2526.horizontalHeaderItem(13)
        item.setText("Nomor Telepon/Handphone")
        item = self.tbl2526.horizontalHeaderItem(14)
        item.setText("Tanggal Daftar")
        self.editBtn_2526.setText("Edit Data")
        self.editBtn_2526.clicked.connect(self.edit2526)
        self.tahunajaran_tab.setTabText(self.tahunajaran_tab.indexOf(self.tab_2526), "2025/2026")
        
    def tampilDataSemuaSiswa2425(self):
        con = sqlite3.connect('ppdb.db')
        cur = con.cursor()
        
        query = "SELECT tb_th2425.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_addsiswa.alamat_siswa, tb_addsiswa.tempat_lahir, tb_addsiswa.tgl_lahir, tb_addsiswa.gender, tb_addsiswa.agama, tb_addsiswa.asal_sekolah, tb_addsiswa.alamat_sekolah, tb_addsiswa.nama_ayah, tb_addsiswa.nama_ibu, tb_addsiswa.penghasilan_ortu, tb_addsiswa.telp_ortu, tb_addsiswa.tgl_daftar FROM tb_th2425 INNER JOIN tb_addsiswa ON tb_th2425.no_daftar = tb_addsiswa.no_daftar ORDER BY tb_th2425.no_daftar DESC;"
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
            self.tbl2425.setItem(baris, 4, QtWidgets.QTableWidgetItem(x[4]))
            self.tbl2425.setItem(baris, 5, QtWidgets.QTableWidgetItem(x[5]))
            self.tbl2425.setItem(baris, 6, QtWidgets.QTableWidgetItem(x[6]))
            self.tbl2425.setItem(baris, 7, QtWidgets.QTableWidgetItem(x[7]))
            self.tbl2425.setItem(baris, 8, QtWidgets.QTableWidgetItem(x[8]))
            self.tbl2425.setItem(baris, 9, QtWidgets.QTableWidgetItem(x[9]))
            self.tbl2425.setItem(baris, 10, QtWidgets.QTableWidgetItem(x[10]))
            self.tbl2425.setItem(baris, 11, QtWidgets.QTableWidgetItem(x[11]))            
            self.tbl2425.setItem(baris, 12, QtWidgets.QTableWidgetItem(x[12]))            
            self.tbl2425.setItem(baris, 13, QtWidgets.QTableWidgetItem(str(x[13])))
            self.tbl2425.setItem(baris, 14, QtWidgets.QTableWidgetItem(x[14]))            
            baris = baris + 1
        # Menyesuaikan lebar kolom dengan panjang karakter data
        self.tbl2425.resizeColumnsToContents()

    def tampilDataSemuaSiswa2526(self):
        con = sqlite3.connect('ppdb.db')
        cur = con.cursor()
        
        query = "SELECT tb_th2526.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_addsiswa.alamat_siswa, tb_addsiswa.tempat_lahir, tb_addsiswa.tgl_lahir, tb_addsiswa.gender, tb_addsiswa.agama, tb_addsiswa.asal_sekolah, tb_addsiswa.alamat_sekolah, tb_addsiswa.nama_ayah, tb_addsiswa.nama_ibu, tb_addsiswa.penghasilan_ortu, tb_addsiswa.telp_ortu, tb_addsiswa.tgl_daftar FROM tb_th2526 INNER JOIN tb_addsiswa ON tb_th2526.no_daftar = tb_addsiswa.no_daftar ORDER BY tb_th2526.no_daftar DESC;"
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
            self.tbl2526.setItem(baris, 4, QtWidgets.QTableWidgetItem(x[4]))
            self.tbl2526.setItem(baris, 5, QtWidgets.QTableWidgetItem(x[5]))
            self.tbl2526.setItem(baris, 6, QtWidgets.QTableWidgetItem(x[6]))
            self.tbl2526.setItem(baris, 7, QtWidgets.QTableWidgetItem(x[7]))
            self.tbl2526.setItem(baris, 8, QtWidgets.QTableWidgetItem(x[8]))
            self.tbl2526.setItem(baris, 9, QtWidgets.QTableWidgetItem(x[9]))
            self.tbl2526.setItem(baris, 10, QtWidgets.QTableWidgetItem(x[10]))
            self.tbl2526.setItem(baris, 11, QtWidgets.QTableWidgetItem(x[11]))            
            self.tbl2526.setItem(baris, 12, QtWidgets.QTableWidgetItem(x[12]))            
            self.tbl2526.setItem(baris, 13, QtWidgets.QTableWidgetItem(str(x[13])))
            self.tbl2526.setItem(baris, 14, QtWidgets.QTableWidgetItem(x[14]))                        
            baris = baris + 1
        # Menyesuaikan lebar kolom dengan panjang karakter data
        self.tbl2526.resizeColumnsToContents()


    def search_data_2425(self):
        keyword = "%" + self.cariEdit_2425.text() + "%"
        query = "SELECT tb_th2425.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_addsiswa.alamat_siswa, tb_addsiswa.tempat_lahir, tb_addsiswa.tgl_lahir, tb_addsiswa.gender, tb_addsiswa.agama, tb_addsiswa.asal_sekolah, tb_addsiswa.alamat_sekolah, tb_addsiswa.nama_ayah, tb_addsiswa.nama_ibu, tb_addsiswa.penghasilan_ortu, tb_addsiswa.telp_ortu FROM tb_th2425 INNER JOIN tb_addsiswa ON tb_th2425.no_daftar = tb_addsiswa.no_daftar;"
        parameter = []

        if keyword:
            query = "SELECT tb_th2425.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_addsiswa.alamat_siswa, tb_addsiswa.tempat_lahir, tb_addsiswa.tgl_lahir, tb_addsiswa.gender, tb_addsiswa.agama, tb_addsiswa.asal_sekolah, tb_addsiswa.alamat_sekolah, tb_addsiswa.nama_ayah, tb_addsiswa.nama_ibu, tb_addsiswa.penghasilan_ortu, tb_addsiswa.telp_ortu FROM tb_th2425 INNER JOIN tb_addsiswa ON tb_th2425.no_daftar = tb_addsiswa.no_daftar WHERE LOWER(tb_th2425.no_daftar) LIKE LOWER(?) OR LOWER(tb_addsiswa.nama_lengkap) LIKE LOWER(?) OR LOWER(tb_addsiswa.nisn_siswa) LIKE LOWER(?) OR LOWER(tb_addsiswa.alamat_siswa) LIKE LOWER(?) OR LOWER(tb_addsiswa.tempat_lahir) LIKE LOWER(?) OR LOWER(tb_addsiswa.tgl_lahir) LIKE LOWER(?) OR LOWER(tb_addsiswa.gender) LIKE LOWER(?) OR LOWER(tb_addsiswa.agama) LIKE LOWER(?) OR LOWER(tb_addsiswa.asal_sekolah) LIKE LOWER(?) OR LOWER(tb_addsiswa.alamat_sekolah) LIKE LOWER(?) OR LOWER(tb_addsiswa.nama_ayah) LIKE LOWER(?) OR LOWER(tb_addsiswa.nama_ibu) LIKE LOWER(?) OR LOWER(tb_addsiswa.penghasilan_ortu) LIKE LOWER(?) OR LOWER(tb_addsiswa.telp_ortu) LIKE LOWER(?);"
            parameter = [keyword] * 14

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
                table_widget.setItem(baris, 4, QtWidgets.QTableWidgetItem(x[4]))
                table_widget.setItem(baris, 5, QtWidgets.QTableWidgetItem(x[5]))
                table_widget.setItem(baris, 6, QtWidgets.QTableWidgetItem(x[6]))
                table_widget.setItem(baris, 7, QtWidgets.QTableWidgetItem(x[7]))
                table_widget.setItem(baris, 8, QtWidgets.QTableWidgetItem(x[8]))
                table_widget.setItem(baris, 9, QtWidgets.QTableWidgetItem(x[9]))
                table_widget.setItem(baris, 10, QtWidgets.QTableWidgetItem(x[10]))
                table_widget.setItem(baris, 11, QtWidgets.QTableWidgetItem(x[11]))
                table_widget.setItem(baris, 12, QtWidgets.QTableWidgetItem(x[12]))
                table_widget.setItem(baris, 13, QtWidgets.QTableWidgetItem(str(x[13])))
                baris = baris + 1

            table_widget.resizeColumnsToContents()

    def search_data_2526(self):
        keyword = "%" + self.cariEdit_2526.text() + "%"
        query = "SELECT tb_th2526.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_addsiswa.alamat_siswa, tb_addsiswa.tempat_lahir, tb_addsiswa.tgl_lahir, tb_addsiswa.gender, tb_addsiswa.agama, tb_addsiswa.asal_sekolah, tb_addsiswa.alamat_sekolah, tb_addsiswa.nama_ayah, tb_addsiswa.nama_ibu, tb_addsiswa.penghasilan_ortu, tb_addsiswa.telp_ortu FROM tb_th2526 INNER JOIN tb_addsiswa ON tb_th2526.no_daftar = tb_addsiswa.no_daftar;"
        parameter = []

        if keyword:
            query = "SELECT tb_th2526.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_addsiswa.alamat_siswa, tb_addsiswa.tempat_lahir, tb_addsiswa.tgl_lahir, tb_addsiswa.gender, tb_addsiswa.agama, tb_addsiswa.asal_sekolah, tb_addsiswa.alamat_sekolah, tb_addsiswa.nama_ayah, tb_addsiswa.nama_ibu, tb_addsiswa.penghasilan_ortu, tb_addsiswa.telp_ortu FROM tb_th2526 INNER JOIN tb_addsiswa ON tb_th2526.no_daftar = tb_addsiswa.no_daftar WHERE LOWER(tb_th2526.no_daftar) LIKE LOWER(?) OR LOWER(tb_addsiswa.nama_lengkap) LIKE LOWER(?) OR LOWER(tb_addsiswa.nisn_siswa) LIKE LOWER(?) OR LOWER(tb_addsiswa.alamat_siswa) LIKE LOWER(?) OR LOWER(tb_addsiswa.tempat_lahir) LIKE LOWER(?) OR LOWER(tb_addsiswa.tgl_lahir) LIKE LOWER(?) OR LOWER(tb_addsiswa.gender) LIKE LOWER(?) OR LOWER(tb_addsiswa.agama) LIKE LOWER(?) OR LOWER(tb_addsiswa.asal_sekolah) LIKE LOWER(?) OR LOWER(tb_addsiswa.alamat_sekolah) LIKE LOWER(?) OR LOWER(tb_addsiswa.nama_ayah) LIKE LOWER(?) OR LOWER(tb_addsiswa.nama_ibu) LIKE LOWER(?) OR LOWER(tb_addsiswa.penghasilan_ortu) LIKE LOWER(?) OR LOWER(tb_addsiswa.telp_ortu) LIKE LOWER(?);"
            parameter = [keyword] * 14

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
                table_widget.setItem(baris, 4, QtWidgets.QTableWidgetItem(x[4]))
                table_widget.setItem(baris, 5, QtWidgets.QTableWidgetItem(x[5]))
                table_widget.setItem(baris, 6, QtWidgets.QTableWidgetItem(x[6]))
                table_widget.setItem(baris, 7, QtWidgets.QTableWidgetItem(x[7]))
                table_widget.setItem(baris, 8, QtWidgets.QTableWidgetItem(x[8]))
                table_widget.setItem(baris, 9, QtWidgets.QTableWidgetItem(x[9]))
                table_widget.setItem(baris, 10, QtWidgets.QTableWidgetItem(x[10]))
                table_widget.setItem(baris, 11, QtWidgets.QTableWidgetItem(x[11]))
                table_widget.setItem(baris, 12, QtWidgets.QTableWidgetItem(x[12]))
                table_widget.setItem(baris, 13, QtWidgets.QTableWidgetItem(str(x[13])))
                baris = baris + 1

            table_widget.resizeColumnsToContents()
            
            
    def edit(self):
        row = self.tbl2425.currentRow()
        print(str(row))
        if row != -1:
            id = self.tbl2425.item(row,0).text()
            nama_siswa = self.tbl2425.item(row,1).text()
            nisn = self.tbl2425.item(row,2).text()
            adres_siswa = self.tbl2425.item(row,3).text()
            tmpt_lahir = self.tbl2425.item(row,4).text()
            tanggal_lahir = self.tbl2425.item(row,5).text()          
            jk = self.tbl2425.item(row,6).text()
            agama_siswa = self.tbl2425.item(row,7).text()
            asal_sklh = self.tbl2425.item(row,8).text()
            adres_sekolah = self.tbl2425.item(row,9).text()
            nm_ayah = self.tbl2425.item(row,10).text()
            nm_ibu = self.tbl2425.item(row,11).text()
            penghasilan = self.tbl2425.item(row,12).text()
            hp_ortu = self.tbl2425.item(row,13).text()
            tanggal_daftar = self.tbl2425.item(row,14).text()
            
            from editdata import editData
            self.ubah = editData()
            self.ubah.nodaftarEdit.setText(id)
            self.ubah.lineEdit_2.setText(tanggal_daftar)
            self.ubah.nm_siswaEdit.setText(nama_siswa)
            self.ubah.nisn_siswaEdit.setText(nisn)
            self.ubah.alamat_siswaEdit.setText(adres_siswa)
            self.ubah.tptlahir_siswaEdit.setText(tmpt_lahir)
            self.ubah.lineEdit_3.setText(tanggal_lahir)          
            self.ubah.lineEdit_4.setText(jk)
            self.ubah.lineEdit_5.setText(agama_siswa)
            self.ubah.nama_sekolahEdit.setText(asal_sklh)
            self.ubah.alamat_sekolahEdit.setText(adres_sekolah)
            self.ubah.nama_ayahEdit.setText(nm_ayah)
            self.ubah.nama_ibuEdit.setText(nm_ibu)
            self.ubah.penghasilan_ortuEdit.setText(penghasilan)
            self.ubah.telp_ortuEdit.setText(hp_ortu)
            self.close()
            
        else:
            QMessageBox.warning(None, "Peringatan", "Pilih satu baris")
            
    def hapus(self):
        row = self.tbl2425.currentRow()
        if row >= 0:  # Periksa apakah ada item yang dipilih
            item = self.tbl2425.item(row, 0)
            if item is not None:  # Periksa apakah item tidak None
                id = item.text()
                mbox = QMessageBox.question(self, "Warning", "Apakah Anda akan menghapus data?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if mbox == QMessageBox.Yes:
                    try:
                        query1 = "DELETE FROM tb_addsiswa WHERE no_daftar=?"
                        query2 = "DELETE FROM tb_th2425 WHERE no_daftar=?"
                        cur.execute(query1, (id,))
                        cur.execute(query2, (id,))
                        con.commit()
                        QMessageBox.information(self, "Perhatian", "Data berhasil dihapus")
                        self.tbl2425.removeRow(row)

                    except:
                        QMessageBox.information(self, "Perhatian", "Data tidak dapat dihapus")
            else:
                QMessageBox.information(self, "Perhatian", "Item tidak tersedia")
        else:
            QMessageBox.information(self, "Perhatian", "Pilih data yang akan dihapus")
            
    def edit2526(self):
        row = self.tbl2526.currentRow()
        print(str(row))
        if row != -1:
            id = self.tbl2526.item(row,0).text()
            nama_siswa = self.tbl2526.item(row,1).text()
            nisn = self.tbl2526.item(row,2).text()
            adres_siswa = self.tbl2526.item(row,3).text()
            tmpt_lahir = self.tbl2526.item(row,4).text()
            tanggal_lahir = self.tbl2526.item(row,5).text()          
            jk = self.tbl2526.item(row,6).text()
            agama_siswa = self.tbl2526.item(row,7).text()
            asal_sklh = self.tbl2526.item(row,8).text()
            adres_sekolah = self.tbl2526.item(row,9).text()
            nm_ayah = self.tbl2526.item(row,10).text()
            nm_ibu = self.tbl2526.item(row,11).text()
            penghasilan = self.tbl2526.item(row,12).text()
            hp_ortu = self.tbl2526.item(row,13).text()
            tanggal_daftar = self.tbl2526.item(row,14).text()
            
            from editdata import editData
            self.ubah = editData()
            self.ubah.nodaftarEdit.setText(id)
            self.ubah.lineEdit_2.setText(tanggal_daftar)
            self.ubah.nm_siswaEdit.setText(nama_siswa)
            self.ubah.nisn_siswaEdit.setText(nisn)
            self.ubah.alamat_siswaEdit.setText(adres_siswa)
            self.ubah.tptlahir_siswaEdit.setText(tmpt_lahir)
            self.ubah.lineEdit_3.setText(tanggal_lahir)          
            self.ubah.lineEdit_4.setText(jk)
            self.ubah.lineEdit_5.setText(agama_siswa)
            self.ubah.nama_sekolahEdit.setText(asal_sklh)
            self.ubah.alamat_sekolahEdit.setText(adres_sekolah)
            self.ubah.nama_ayahEdit.setText(nm_ayah)
            self.ubah.nama_ibuEdit.setText(nm_ibu)
            self.ubah.penghasilan_ortuEdit.setText(penghasilan)
            self.ubah.telp_ortuEdit.setText(hp_ortu)
            self.close()
            
        else:
            QMessageBox.warning(None, "Peringatan", "Pilih satu baris")
            
    def hapus2526(self):
        row = self.tbl2526.currentRow()
        if row >= 0:  # Periksa apakah ada item yang dipilih
            item = self.tbl2526.item(row, 0)
            if item is not None:  # Periksa apakah item tidak None
                id = item.text()
                mbox = QMessageBox.question(self, "Warning", "Apakah Anda akan menghapus data?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

                if mbox == QMessageBox.Yes:
                    try:
                        query1 = "DELETE FROM tb_addsiswa WHERE no_daftar=?"
                        query2 = "DELETE FROM tb_th2526 WHERE no_daftar=?"
                        cur.execute(query1, (id,))
                        cur.execute(query2, (id,))
                        con.commit()
                        QMessageBox.information(self, "Perhatian", "Data berhasil dihapus")
                        self.tbl2526.removeRow(row)

                    except:
                        QMessageBox.information(self, "Perhatian", "Data tidak dapat dihapus")
            else:
                QMessageBox.information(self, "Perhatian", "Item tidak tersedia")
        else:
            QMessageBox.information(self, "Perhatian", "Pilih data yang akan dihapus")
            
    def kembali(self):
        # Import modul subprocess
        import subprocess

        # Membuka file window.py
        subprocess.Popen(["python", "window.py"])

        # Menutup semuasiswa.py
        sys.exit()
     
def main():
    APP = QApplication(sys.argv)
    window = semuaSiswa()
    window.show()
    sys.exit(APP.exec())
    
if __name__ == '__main__':
    main()