from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dbmanager import DBManager

class Ui_Dialog_Bonsa_Details(object):
    
    def setToday_1(self):
        self.dateEdit_1.setDate(QtCore.QDate.currentDate())
        
    def setToday_2(self):
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
        
    def del_details(self):
        try:
            self.selected = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
            self.selected_row = self.tableWidget.currentRow()
            self.dbManager.connect()
            self.query = "delete from Bonsa where id = ?"
            self.dbManager.cursor.execute(self.query, (self.selected))
            self.dbManager.conn.commit()
            self.dbManager.close()
            self.tableWidget.removeRow(self.selected_row)
            msg = QMessageBox()
            msg.setWindowTitle("삭제완료")
            msg.setText("삭제 되었습니다.")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("오류")
            msg.setText("삭제할 항목을 선택하세요")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec()
        
    def search_product(self):
        self.date1 = self.dateEdit_1.date().toString('yyyy-MM-dd')
        self.date2 = self.dateEdit_2.date().toString('yyyy-MM-dd')
        self.name = self.cBox_name.currentText()
        
        if self.name == "전체":
            self.tableWidget.clearContents()
            self.dbManager.connect()
            
            self.query = "Select sum(Price), sum(Cashin) from Bonsa where Date between ? and ?"
            self.result = self.dbManager.cursor.execute(self.query, self.date1, self.date2)
            for i in self.result:
                if i[0] != None:
                    self.total_price = i[0]
                else:
                    self.total_price = "0"
                if i[1] != None:
                    self.total_cashin = i[1]
                else:
                    self.total_cashin = "0"

            self.label_total_a.setText(format(int(self.total_price),','))
            self.label_total_b.setText(format(int(self.total_cashin),','))
            
            self.query = "Select id, Date, Name, Product, Pin, Price, Percentage, Cashin from Bonsa where Date between ? and ? order by Date, id"
            self.dbManager.cursor.execute(self.query, self.date1, self.date2)
            self.rows = self.dbManager.cursor.fetchall()
            self.tableWidget.setRowCount(len(self.rows))
            
            self.tbrow = 0
            for i in self.rows:
                if i[3] == None:
                    pr = ""
                else:
                    pr = str(i[3])
                if i[4] == None:
                    pin = ""
                else:
                    pin = str(i[4])
                if i[5] != None:
                    price = format(i[5],',')
                else:
                    price = ""
                if i[6] == None:
                    percent = ""
                else:
                    percent = str(i[6])
                if i[7] != None:
                    cashin = format(i[7],',')
                else:
                    cashin = ""
                item = QtWidgets.QTableWidgetItem(str(i[0]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 0, item)
                item = QtWidgets.QTableWidgetItem(str(i[1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 1, item)
                item = QtWidgets.QTableWidgetItem(str(i[2]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 2, item)
                item = QtWidgets.QTableWidgetItem(pr)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 3, item)
                item = QtWidgets.QTableWidgetItem(pin)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 4, item)
                item = QtWidgets.QTableWidgetItem(price)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 5, item)
                item = QtWidgets.QTableWidgetItem(percent)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 6, item)
                item = QtWidgets.QTableWidgetItem(cashin)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 7, item)
                self.tbrow += 1
            self.dbManager.close()
        else:
            self.tableWidget.clearContents()
            self.dbManager.connect()
            
            self.query = "Select sum(Price), sum(Cashin) from Bonsa where Date between ? and ? and Name = ?"
            self.result = self.dbManager.cursor.execute(self.query, self.date1, self.date2, self.name)
            for i in self.result:
                if i[0] != None:
                    self.total_price = i[0]
                else:
                    self.total_price = "0"
                if i[1] != None:
                    self.total_cashin = i[1]
                else:
                    self.total_cashin = "0"

            self.label_total_a.setText(format(int(self.total_price),','))
            self.label_total_b.setText(format(int(self.total_cashin),','))
            
            self.query = "Select id, Date, Name, Product, Pin, Price, Percentage, Cashin from Bonsa where Date between ? and ? and Name = ? order by Date, id"
            self.dbManager.cursor.execute(self.query, self.date1, self.date2, self.name)
            self.rows = self.dbManager.cursor.fetchall()
            self.tableWidget.setRowCount(len(self.rows))

            self.tbrow = 0
            for i in self.rows:
                if i[3] == None:
                    pr = ""
                else:
                    pr = str(i[3])
                if i[4] == None:
                    pin = ""
                else:
                    pin = str(i[4])
                if i[5] != None:
                    price = format(i[5],',')
                else:
                    price = ""
                if i[6] == None:
                    percent = ""
                else:
                    percent = str(i[6])
                if i[7] != None:
                    cashin = format(i[7],',')
                else:
                    cashin = ""
                    
                item = QtWidgets.QTableWidgetItem(str(i[0]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 0, item)
                item = QtWidgets.QTableWidgetItem(str(i[1]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 1, item)
                item = QtWidgets.QTableWidgetItem(str(i[2]))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 2, item)
                item = QtWidgets.QTableWidgetItem(pr)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 3, item)
                item = QtWidgets.QTableWidgetItem(pin)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 4, item)
                item = QtWidgets.QTableWidgetItem(price)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 5, item)
                item = QtWidgets.QTableWidgetItem(percent)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 6, item)
                item = QtWidgets.QTableWidgetItem(cashin)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 7, item)
                self.tbrow += 1
            self.dbManager.close()
    
    def setupUi(self, Dialog_Bonsa_Details):
        Dialog_Bonsa_Details.setObjectName("Dialog_Bonsa_Details")
        Dialog_Bonsa_Details.resize(1063, 863)
        self.cBox_name = QtWidgets.QComboBox(Dialog_Bonsa_Details)
        self.cBox_name.setGeometry(QtCore.QRect(610, 764, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cBox_name.setFont(font)
        self.cBox_name.setEditable(False)
        self.cBox_name.setModelColumn(0)
        self.cBox_name.setObjectName("cBox_name")
        self.dbManager = DBManager()
        self.dateEdit_1 = QtWidgets.QDateEdit(Dialog_Bonsa_Details)
        self.dateEdit_1.setGeometry(QtCore.QRect(260, 760, 121, 41))
        self.dateEdit_1.setFocusPolicy(QtCore.Qt.NoFocus)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_1.setFont(font)
        self.dateEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_1.setReadOnly(False)
        self.dateEdit_1.setCalendarPopup(True)
        self.dateEdit_1.setObjectName("dateEdit_1")
        self.btn_delete = QtWidgets.QPushButton(Dialog_Bonsa_Details, clicked = self.del_details)
        self.btn_delete.setGeometry(QtCore.QRect(70, 766, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setAutoDefault(False)
        self.btn_delete.setDefault(False)
        self.btn_delete.setFlat(False)
        self.btn_delete.setObjectName("btn_delete")
        self.label_11 = QtWidgets.QLabel(Dialog_Bonsa_Details)
        self.label_11.setGeometry(QtCore.QRect(390, 769, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog_Bonsa_Details)
        self.dateEdit_2.setGeometry(QtCore.QRect(440, 760, 121, 41))
        self.dateEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setReadOnly(False)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.tableWidget = QtWidgets.QTableWidget(Dialog_Bonsa_Details)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1021, 661))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnWidth(1, 110)
        self.tableWidget.setColumnWidth(3, 220)
        self.tableWidget.setColumnWidth(5, 140)
        self.tableWidget.setColumnWidth(7, 120)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label = QtWidgets.QLabel(Dialog_Bonsa_Details)
        self.label.setGeometry(QtCore.QRect(200, 700, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_total_a = QtWidgets.QLabel(Dialog_Bonsa_Details)
        self.label_total_a.setGeometry(QtCore.QRect(320, 700, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_a.setFont(font)
        self.label_total_a.setText("")
        self.label_total_a.setObjectName("label_total_a")

        self.label2 = QtWidgets.QLabel(Dialog_Bonsa_Details)
        self.label2.setGeometry(QtCore.QRect(520, 700, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label_total_b = QtWidgets.QLabel(Dialog_Bonsa_Details)
        self.label_total_b.setGeometry(QtCore.QRect(640, 700, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_b.setFont(font)
        self.label_total_b.setText("")
        self.label_total_b.setObjectName("label_total_b")


        self.btn_search = QtWidgets.QPushButton(Dialog_Bonsa_Details, clicked = self.search_product)
        self.btn_search.setGeometry(QtCore.QRect(760, 750, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setAutoDefault(False)
        self.btn_search.setDefault(False)
        self.btn_search.setFlat(False)
        self.btn_search.setObjectName("btn_search")
        
        self.dateEdit_1.setDate(QtCore.QDate.currentDate())
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
        self._today_button_1 = QtWidgets.QPushButton('&오늘', clicked=self.setToday_1)
        self.dateEdit_1.calendarWidget().layout().addWidget(self._today_button_1)
        self._today_button_2 = QtWidgets.QPushButton('&오늘', clicked=self.setToday_2)
        self.dateEdit_2.calendarWidget().layout().addWidget(self._today_button_2)
        
        self.dateEdit_1.wheelEvent = lambda event: None
        self.dateEdit_2.wheelEvent = lambda event: None
        self.cBox_name.wheelEvent = lambda event: None

        self.retranslateUi(Dialog_Bonsa_Details)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Bonsa_Details)

    def retranslateUi(self, Dialog_Bonsa_Details):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Bonsa_Details.setWindowTitle(_translate("Dialog_Bonsa_Details", "Dialog"))
        self.btn_delete.setText(_translate("Dialog_Bonsa_Details", "삭제"))
        self.label_11.setText(_translate("Dialog_Bonsa_Details", "~"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_Bonsa_Details", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_Bonsa_Details", "날짜"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_Bonsa_Details", "본사명"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog_Bonsa_Details", "제품명"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog_Bonsa_Details", "수량"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog_Bonsa_Details", "A가"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog_Bonsa_Details", "적용%"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog_Bonsa_Details", "입금"))
        self.label.setText(_translate("Dialog_Bonsa_Details", "총 입고 합계: "))
        self.label2.setText(_translate("Dialog_Bonsa_Details", "입금 합계: "))
        self.btn_search.setText(_translate("Dialog_Bonsa_Details", "조회"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Bonsa_Details = QtWidgets.QDialog()
    ui = Ui_Dialog_Bonsa_Details()
    ui.setupUi(Dialog_Bonsa_Details)
    Dialog_Bonsa_Details.show()
    sys.exit(app.exec_())
