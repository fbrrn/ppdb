import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from window import windowAdmin

import sqlite3
con = sqlite3.connect('ppdb.db')
cur = con.cursor()

class inputHasil(QWidget):
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
        self.inputHasilSeleksi_2425()
        self.inputHasilSeleksi_2526()
        
    def closeEvent(self, event):
        self.mainwin = windowAdmin()

    def setupUi(self):
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton = QtWidgets.QToolButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.toolButton.setFont(font)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        self.horizontalLayout.addWidget(self.widget_3, 0, QtCore.Qt.AlignVCenter)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
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
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.widget_4, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.simpanBtn_2425 = QtWidgets.QPushButton(self.tab_2425)
        self.simpanBtn_2425.setObjectName("simpanBtn_2425")
        self.gridLayout_2.addWidget(self.simpanBtn_2425, 2, 0, 1, 1)
        self.widget_5 = QtWidgets.QWidget(self.tab_2425)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout.setObjectName("gridLayout")
        self.cariBtn_2425 = QtWidgets.QPushButton(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cariBtn_2425.setFont(font)
        self.cariBtn_2425.setObjectName("cariBtn_2425")
        self.gridLayout.addWidget(self.cariBtn_2425, 0, 2, 1, 1)
        self.cariLbl = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cariLbl.setFont(font)
        self.cariLbl.setObjectName("cariLbl")
        self.gridLayout.addWidget(self.cariLbl, 0, 0, 1, 1)
        self.cariEdit_2425 = QtWidgets.QLineEdit(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cariEdit_2425.setFont(font)
        self.cariEdit_2425.setObjectName("cariEdit_2425")
        self.gridLayout.addWidget(self.cariEdit_2425, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.widget_5, 0, 0, 1, 1)
        self.batalBtn_2425 = QtWidgets.QPushButton(self.tab_2425)
        self.batalBtn_2425.setObjectName("batalBtn_2425")
        self.gridLayout_2.addWidget(self.batalBtn_2425, 3, 0, 1, 1)
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
        self.widget_6 = QtWidgets.QWidget(self.tab_2526)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)
        self.cariEdit_2526 = QtWidgets.QLineEdit(self.widget_6)
        self.cariEdit_2526.setObjectName("cariEdit_2526")
        self.gridLayout_8.addWidget(self.cariEdit_2526, 0, 1, 1, 1)
        self.cariBtn_2526 = QtWidgets.QPushButton(self.widget_6)
        self.cariBtn_2526.setObjectName("cariBtn_2526")
        self.gridLayout_8.addWidget(self.cariBtn_2526, 0, 2, 1, 1)
        self.gridLayout_3.addWidget(self.widget_6, 0, 0, 1, 1)
        self.batalBtn_2526 = QtWidgets.QPushButton(self.tab_2526)
        self.batalBtn_2526.setObjectName("batalBtn_2526")
        self.gridLayout_3.addWidget(self.batalBtn_2526, 3, 0, 1, 1)
        self.simpanBtn_2526 = QtWidgets.QPushButton(self.tab_2526)
        self.simpanBtn_2526.setObjectName("simpanBtn_2526")
        self.gridLayout_3.addWidget(self.simpanBtn_2526, 2, 0, 1, 1)
        self.tahunajaran_tab.addTab(self.tab_2526, "")
        self.verticalLayout.addWidget(self.tahunajaran_tab)
        self.verticalLayout_2.addWidget(self.widget_2)

        self.tahunajaran_tab.setCurrentIndex(0)
        self.setLayout(self.verticalLayout_2)
        
    def retranslateUi(self):
        self.toolButton.setText("KEMBALI")
        self.toolButton.clicked.connect(self.kembali)
        
        self.label.setText("INPUT HASIL SELEKSI")
        self.tbl2425.setSortingEnabled(True)
        item = self.tbl2425.horizontalHeaderItem(0)
        item.setText("No Pendaftaran")
        item = self.tbl2425.horizontalHeaderItem(1)
        item.setText("Nama Lengkap")
        item = self.tbl2425.horizontalHeaderItem(2)
        item.setText("NISN")
        item = self.tbl2425.horizontalHeaderItem(3)
        item.setText("Keterangan")
        self.cariBtn_2425.setText("Cari")
        self.cariBtn_2425.clicked.connect(self.search_data_2425)
        self.cariLbl.setText("Pencarian")
        self.simpanBtn_2425.setText("Simpan")
        self.simpanBtn_2425.clicked.connect(self.simpanInput_2425)
        self.batalBtn_2425.setText("Batal")
        self.batalBtn_2425.clicked.connect(self.kembali)
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
        self.label_2.setText("Pencarian")
        self.cariBtn_2526.setText("Cari")
        self.cariBtn_2526.clicked.connect(self.search_data_2526)
        self.batalBtn_2526.setText("Batal")
        self.batalBtn_2526.clicked.connect(self.kembali)
        self.simpanBtn_2526.setText("Simpan")
        self.simpanBtn_2526.clicked.connect(self.simpanInput_2526)
        self.tahunajaran_tab.setTabText(self.tahunajaran_tab.indexOf(self.tab_2526), "2025/2026")
        
    def inputHasilSeleksi_2425(self):        
        query = "SELECT tb_th2425.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_th2425.keterangan FROM tb_th2425 INNER JOIN tb_addsiswa ON tb_th2425.no_daftar = tb_addsiswa.no_daftar ORDER BY tb_th2425.no_daftar DESC;"
        cur.execute(query)
        data_input = cur.fetchall()

        self.tbl2425.setRowCount(len(data_input))
        self.tbl2425.setColumnCount(4)

        updated_data = set()  # Set to store the updated data

        for row, data in enumerate(data_input):
            self.tbl2425.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.tbl2425.setItem(row, 1, QtWidgets.QTableWidgetItem(data[1]))
            self.tbl2425.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))

            combo_box = QtWidgets.QComboBox()
            combo_box.addItem("Diterima")
            combo_box.addItem("Ditolak")

            # Check if the data has been updated
            if data[3] is not None:
                combo_box.setCurrentText(data[3])  # Set the combo box value
                combo_box.setDisabled(True)  # Disable the combo box

            self.tbl2425.setCellWidget(row, 3, combo_box)

            updated_data.add(data[0])  # Add the updated data to the set

        # Set the column headers
        item = QtWidgets.QTableWidgetItem()
        item.setText("No Pendaftaran")
        self.tbl2425.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("Nama Siswa")
        self.tbl2425.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("NISN")
        self.tbl2425.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("Keterangan")
        self.tbl2425.setHorizontalHeaderItem(3, item)

        self.tbl2425.resizeColumnsToContents()
        
    def inputHasilSeleksi_2526(self):        
        query = "SELECT tb_th2526.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa, tb_th2526.keterangan FROM tb_th2526 INNER JOIN tb_addsiswa ON tb_th2526.no_daftar = tb_addsiswa.no_daftar ORDER BY tb_th2526.no_daftar DESC;"
        cur.execute(query)
        data_input = cur.fetchall()

        self.tbl2526.setRowCount(len(data_input))
        self.tbl2526.setColumnCount(4)

        updated_data = set()  # Set to store the updated data

        for row, data in enumerate(data_input):
            self.tbl2526.setItem(row, 0, QtWidgets.QTableWidgetItem(str(data[0])))
            self.tbl2526.setItem(row, 1, QtWidgets.QTableWidgetItem(data[1]))
            self.tbl2526.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data[2])))

            combo_box = QtWidgets.QComboBox()
            combo_box.addItem("Diterima")
            combo_box.addItem("Ditolak")

            # Check if the data has been updated
            if data[3] is not None:
                combo_box.setCurrentText(data[3])  # Set the combo box value
                combo_box.setDisabled(True)  # Disable the combo box

            self.tbl2526.setCellWidget(row, 3, combo_box)

            updated_data.add(data[0])  # Add the updated data to the set

        # Set the column headers
        item = QtWidgets.QTableWidgetItem()
        item.setText("No Pendaftaran")
        self.tbl2526.setHorizontalHeaderItem(0, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("Nama Siswa")
        self.tbl2526.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("NISN")
        self.tbl2526.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        item.setText("Keterangan")
        self.tbl2526.setHorizontalHeaderItem(3, item)

        self.tbl2526.resizeColumnsToContents()

    def simpanInput_2425(self):
        for row in range(self.tbl2425.rowCount()):
            no_daftar = self.tbl2425.item(row, 0).text()
            keterangan = self.tbl2425.cellWidget(row, 3).currentText()
            
            # Periksa data keterangan sebelumnya
            query_sebelumnya = f"SELECT keterangan FROM tb_th2425 WHERE no_daftar = {no_daftar};"
            cur.execute(query_sebelumnya)
            data_sebelumnya = cur.fetchone()
            
            # Jika data sebelumnya ada dan sama dengan keterangan yang akan disimpan, abaikan perubahan
            if data_sebelumnya and data_sebelumnya[0] == keterangan:
                continue
            
            # Lakukan perubahan pada database
            query = f"UPDATE tb_th2425 SET keterangan = '{keterangan}' WHERE no_daftar = {no_daftar};"
            cur.execute(query)
            
        con.commit()  # Commit the changes
                        
        QMessageBox.information(None, "Informasi", "Data berhasil disimpan")

    def simpanInput_2526(self):
        for row in range(self.tbl2526.rowCount()):
            no_daftar = self.tbl2526.item(row, 0).text()
            keterangan = self.tbl2526.cellWidget(row, 3).currentText()
            
            # Periksa data keterangan sebelumnya
            query_sebelumnya = f"SELECT keterangan FROM tb_th2526 WHERE no_daftar = {no_daftar};"
            cur.execute(query_sebelumnya)
            data_sebelumnya = cur.fetchone()
            
            # Jika data sebelumnya ada dan sama dengan keterangan yang akan disimpan, abaikan perubahan
            if data_sebelumnya and data_sebelumnya[0] == keterangan:
                continue
            
            # Lakukan perubahan pada database
            query = f"UPDATE tb_th2526 SET keterangan = '{keterangan}' WHERE no_daftar = {no_daftar};"
            cur.execute(query)
    
            con.commit()  # Commit the changes
                        
        QMessageBox.information(None, "Informasi", "Data berhasil disimpan")
   
    def search_data_2425(self):
        keyword = "%" + self.cariEdit_2425.text() + "%"
        query = "SELECT tb_th2425.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa FROM tb_th2425 INNER JOIN tb_addsiswa ON tb_th2425.no_daftar = tb_addsiswa.no_daftar;"
        parameter = []

        if keyword:
            query = "SELECT tb_th2425.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa FROM tb_th2425 INNER JOIN tb_addsiswa ON tb_th2425.no_daftar = tb_addsiswa.no_daftar WHERE LOWER(tb_th2425.no_daftar) LIKE LOWER(?) OR LOWER(tb_addsiswa.nama_lengkap) LIKE LOWER(?) OR LOWER(tb_addsiswa.nisn_siswa) LIKE LOWER(?);"
            parameter = [keyword] * 3

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
                baris = baris + 1

            table_widget.resizeColumnsToContents()

    def search_data_2526(self):
        keyword = "%" + self.cariEdit_2526.text() + "%"
        query = "SELECT tb_th2526.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa FROM tb_th2526 INNER JOIN tb_addsiswa ON tb_th2526.no_daftar = tb_addsiswa.no_daftar;"
        parameter = []

        if keyword:
            query = "SELECT tb_th2526.no_daftar, tb_addsiswa.nama_lengkap, tb_addsiswa.nisn_siswa FROM tb_th2526 INNER JOIN tb_addsiswa ON tb_th2526.no_daftar = tb_addsiswa.no_daftar WHERE LOWER(tb_th2526.no_daftar) LIKE LOWER(?) OR LOWER(tb_addsiswa.nama_lengkap) LIKE LOWER(?) OR LOWER(tb_addsiswa.nisn_siswa) LIKE LOWER(?);"
            parameter = [keyword] * 3

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
                baris = baris + 1

            table_widget.resizeColumnsToContents()
                                                   
    def kembali(self):
        self.close()
     
def main():
    APP = QApplication(sys.argv)
    window = inputHasil()
    window.show()
    sys.exit(APP.exec())
    
if __name__ == '__main__':
    main()