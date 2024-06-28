from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dbmanager import DBManager, PrintManager

class Ui_Dialog_Branch_Details(object):
    
    def setToday_1(self):
        self.dateEdit_1.setDate(QtCore.QDate.currentDate())
        
    def setToday_2(self):
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
        
    def del_details(self):
        try:
            self.selected = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
            self.selected_row = self.tableWidget.currentRow()
            self.dbManager.connect()
            self.query = "delete from Branch where id = ?"
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
            
            self.query = "Select sum(Sales), sum(Cashin) from Branch where Date between ? and ?"
            self.result = self.dbManager.cursor.execute(self.query, self.date1, self.date2)
            for i in self.result:
                if i[0] != None:
                    self.total_sales = i[0]
                else:
                    self.total_sales = "0"
                if i[1] != None:
                    self.total_cashin = i[1]
                else:
                    self.total_cashin = "0"

            self.label_total_a.setText(format(int(self.total_sales),','))
            self.label_total_in.setText(format(int(self.total_cashin),','))
            self.label_total_misu.setText(format(int(self.total_sales)-int(self.total_cashin),','))

            self.query = "Select sum(Sales), sum(Cashin) from Branch"
            self.result = self.dbManager.cursor.execute(self.query)
            for i in self.result:
                if i[0] != None:
                    self.total_sales = i[0]
                else:
                    self.total_sales = "0"
                if i[1] != None:
                    self.total_cashin = i[1]
                else:
                    self.total_cashin = "0"

            self.label_final_misu.setText(format(int(self.total_sales)-int(self.total_cashin),','))
            
            self.query = "Select id, Date, Name, Product, Pout, Sales, Percentage, Cashin, Etcc from Branch where Date between ? and ? order by Date, id"
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
                    pout = ""
                else:
                    pout = str(i[4])
                if i[5] != None:
                    sales = format(i[5],',')
                else:
                    sales = ""
                if i[6] == None:
                    percent = ""
                else:
                    percent = str(i[6])
                if i[7] != None:
                    cashin = format(i[7],',')
                else:
                    cashin = ""
                if i[8] == None:
                    etc = ""
                else:
                    etc = str(i[8])
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
                item = QtWidgets.QTableWidgetItem(pout)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 4, item)
                item = QtWidgets.QTableWidgetItem(sales)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 5, item)
                item = QtWidgets.QTableWidgetItem(percent)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 6, item)
                item = QtWidgets.QTableWidgetItem(cashin)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 7, item)
                item = QtWidgets.QTableWidgetItem(etc)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 8, item)
                self.tbrow += 1
            self.dbManager.close()
        else:
            self.tableWidget.clearContents()
            self.dbManager.connect()
            
            self.query = "Select sum(Sales), sum(Cashin) from Branch where Date between ? and ? and Name = ?"
            self.result = self.dbManager.cursor.execute(self.query, self.date1, self.date2, self.name)
            for i in self.result:
                if i[0] != None:
                    self.total_sales = i[0]
                else:
                    self.total_sales = "0"
                if i[1] != None:
                    self.total_cashin = i[1]
                else:
                    self.total_cashin = "0"

            self.label_total_a.setText(format(int(self.total_sales),','))
            self.label_total_in.setText(format(int(self.total_cashin),','))
            self.label_total_misu.setText(format(int(self.total_sales)-int(self.total_cashin),','))

            self.query = "Select sum(Sales), sum(Cashin) from Branch where Name = ?"
            self.result = self.dbManager.cursor.execute(self.query, self.name)
            for i in self.result:
                if i[0] != None:
                    self.total_sales = i[0]
                else:
                    self.total_sales = "0"
                if i[1] != None:
                    self.total_cashin = i[1]
                else:
                    self.total_cashin = "0"

            self.label_final_misu.setText(format(int(self.total_sales)-int(self.total_cashin),','))
            
            self.query = "Select id, Date, Name, Product, Pout, Sales, Percentage, Cashin, Etcc from Branch where Date between ? and ? and Name = ? order by Date, id"
            self.dbManager.cursor.execute(self.query, (self.date1, self.date2, self.name))
            self.rows = self.dbManager.cursor.fetchall()
            self.tableWidget.setRowCount(len(self.rows))

            self.tbrow = 0
            for i in self.rows:
                if i[3] == None:
                    pr = ""
                else:
                    pr = str(i[3])
                if i[4] == None:
                    pout = "0"
                else:
                    pout = str(i[4])
                if i[5] != None:
                    sales = format(i[5],',')
                else:
                    sales = "0"
                if i[6] == None:
                    percent = "0"
                else:
                    percent = str(i[6])
                if i[7] != None:
                    cashin = format(i[7],',')
                else:
                    cashin = "0"
                if i[8] == None:
                    etc = ""
                else:
                    etc = str(i[8])
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
                item = QtWidgets.QTableWidgetItem(pout)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 4, item)
                item = QtWidgets.QTableWidgetItem(sales)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 5, item)
                item = QtWidgets.QTableWidgetItem(percent)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 6, item)
                item = QtWidgets.QTableWidgetItem(cashin)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 7, item)
                item = QtWidgets.QTableWidgetItem(etc)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(self.tbrow, 8, item)
                self.tbrow += 1
            self.dbManager.close()
    
    
    def setupUi(self, Dialog_Branch_Details):
        Dialog_Branch_Details.setObjectName("Dialog_Branch_Details")
        Dialog_Branch_Details.resize(1131, 860)
        self.btn_delete = QtWidgets.QPushButton(Dialog_Branch_Details, clicked = self.del_details)
        self.btn_delete.setGeometry(QtCore.QRect(50, 766, 61, 41))
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
        self.dbManager = DBManager()
        self.printManager = PrintManager()
        self.tableWidget = QtWidgets.QTableWidget(Dialog_Branch_Details)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1111, 661))
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
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(0, 82)
        self.tableWidget.setColumnWidth(1, 110)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 260)
        self.tableWidget.setColumnWidth(4, 80)
        self.tableWidget.setColumnWidth(5, 120)
        self.tableWidget.setColumnWidth(6, 70)
        self.tableWidget.setColumnWidth(7, 120)
        self.tableWidget.setColumnWidth(8, 130)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.label_11 = QtWidgets.QLabel(Dialog_Branch_Details)
        self.label_11.setGeometry(QtCore.QRect(320, 769, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog_Branch_Details)
        self.dateEdit_2.setGeometry(QtCore.QRect(370, 760, 121, 41))
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
        self.btn_search = QtWidgets.QPushButton(Dialog_Branch_Details, clicked = self.search_product)
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
        self.cBox_name = QtWidgets.QComboBox(Dialog_Branch_Details)
        self.cBox_name.setGeometry(QtCore.QRect(570, 764, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cBox_name.setFont(font)
        self.cBox_name.setEditable(False)
        self.cBox_name.setModelColumn(0)
        self.cBox_name.setObjectName("cBox_name")
        
        self.dateEdit_1 = QtWidgets.QDateEdit(Dialog_Branch_Details)
        self.dateEdit_1.setGeometry(QtCore.QRect(190, 760, 121, 41))
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
        self.label = QtWidgets.QLabel(Dialog_Branch_Details)
        self.label.setGeometry(QtCore.QRect(50, 700, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog_Branch_Details)
        self.label_2.setGeometry(QtCore.QRect(300, 700, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_Branch_Details)
        self.label_3.setGeometry(QtCore.QRect(550, 700, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog_Branch_Details)
        self.label_4.setGeometry(QtCore.QRect(800, 700, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_total_a = QtWidgets.QLabel(Dialog_Branch_Details)
        self.label_total_a.setGeometry(QtCore.QRect(150, 700, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_a.setFont(font)
        self.label_total_a.setText("")
        self.label_total_a.setObjectName("label_total_a")
        self.label_total_in = QtWidgets.QLabel(Dialog_Branch_Details)
        self.label_total_in.setGeometry(QtCore.QRect(400, 700, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_in.setFont(font)
        self.label_total_in.setText("")
        self.label_total_in.setObjectName("label_total_in")
        self.label_total_misu = QtWidgets.QLabel(Dialog_Branch_Details)
        self.label_total_misu.setGeometry(QtCore.QRect(650, 700, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_misu.setFont(font)
        self.label_total_misu.setText("")
        self.label_total_misu.setObjectName("label_total_misu")

        self.label_final_misu = QtWidgets.QLabel(Dialog_Branch_Details)
        self.label_final_misu.setGeometry(QtCore.QRect(900, 700, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_final_misu.setFont(font)
        self.label_final_misu.setText("")
        self.label_final_misu.setObjectName("label_final_misu")
        
        self.dateEdit_1.setDate(QtCore.QDate.currentDate())
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
        self._today_button_1 = QtWidgets.QPushButton('&오늘', clicked=self.setToday_1)
        self.dateEdit_1.calendarWidget().layout().addWidget(self._today_button_1)
        self._today_button_2 = QtWidgets.QPushButton('&오늘', clicked=self.setToday_2)
        self.dateEdit_2.calendarWidget().layout().addWidget(self._today_button_2)
        
        self.dateEdit_1.wheelEvent = lambda event: None
        self.dateEdit_2.wheelEvent = lambda event: None
        self.cBox_name.wheelEvent = lambda event: None

        self.retranslateUi(Dialog_Branch_Details)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Branch_Details)

    def retranslateUi(self, Dialog_Branch_Details):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Branch_Details.setWindowTitle(_translate("Dialog_Branch_Details", "Dialog"))
        self.btn_delete.setText(_translate("Dialog_Branch_Details", "삭제"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_Branch_Details", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_Branch_Details", "날짜"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_Branch_Details", "지사명"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog_Branch_Details", "제품명"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog_Branch_Details", "수량"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog_Branch_Details", "A가"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog_Branch_Details", "적용%"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Dialog_Branch_Details", "입금액"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Dialog_Branch_Details", "비고"))
        self.label_11.setText(_translate("Dialog_Branch_Details", "~"))
        self.btn_search.setText(_translate("Dialog_Branch_Details", "조회"))
        self.label.setText(_translate("Dialog_Branch_Details", "총 A가 합계: "))
        self.label_2.setText(_translate("Dialog_Branch_Details", "총 입금액: "))
        self.label_3.setText(_translate("Dialog_Branch_Details", "기간미수: "))
        self.label_4.setText(_translate("Dialog_Branch_Details", "누적미수: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Branch_Details = QtWidgets.QDialog()
    ui = Ui_Dialog_Branch_Details()
    ui.setupUi(Dialog_Branch_Details)
    Dialog_Branch_Details.show()
    sys.exit(app.exec_())
