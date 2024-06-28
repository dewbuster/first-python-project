from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dbmanager import DBManager
import datetime

class Ui_Dialog_Card_Details(object):
    
    def setToday_1(self):
        self.dateEdit_1.setDate(QtCore.QDate.currentDate())
    def setToday_2(self):
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
    def setToday_3(self):
        self.dateEdit_3.setDate(QtCore.QDate.currentDate())

    def check_card(self):
        try:
            self.date3 = self.dateEdit_3.date().toString('yyyy-MM-dd')
            self.selected = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
            self.dbManager.connect()
            self.query = "UPDATE Staff SET Cardcheck = ? where id = ?"
            self.dbManager.cursor.execute(self.query, (self.date3, self.selected))
            self.dbManager.conn.commit()
            self.dbManager.close()
            item = QtWidgets.QTableWidgetItem(self.date3)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(self.tableWidget.currentRow(), 6, item)
            msg = QMessageBox()
            msg.setWindowTitle("확인완료")
            msg.setText("입력 되었습니다.")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("오류")
            msg.setText("항목을 선택하세요")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec()

    def cancel_card(self):
        try:
            self.date3 = ''
            self.selected = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
            self.dbManager.connect()
            self.query = "UPDATE Staff SET Cardcheck = NULL where id = ?"
            self.dbManager.cursor.execute(self.query, (self.selected))
            self.dbManager.conn.commit()
            self.dbManager.close()
            item = QtWidgets.QTableWidgetItem(self.date3)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(self.tableWidget.currentRow(), 6, item)
            msg = QMessageBox()
            msg.setWindowTitle("확인완료")
            msg.setText("입력 되었습니다.")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("오류")
            msg.setText("항목을 선택하세요")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec()
        
    def search_details(self):
        self.date1 = self.dateEdit_1.date().toString('yyyy-MM-dd')
        self.date2 = self.dateEdit_2.date().toString('yyyy-MM-dd')
        self.tableWidget.clearContents()
        self.dbManager.connect()

        self.query = "Select sum(Cardin) from Staff where Cardin != 0 and Number != 0 and Date between ? and ?"
        self.result = self.dbManager.cursor.execute(self.query, (self.date1, self.date2)).fetchall()
        for i in self.result:
            if i[0] != None:
                    self.total_cardin = i[0]
            else:
                self.total_cardin = "0"

        self.label_calc.setText("합계: " + format(int(self.total_cardin),','))
        
        self.query = "select id, Date, Cardin, Number, Cardkind, Name, Cardcheck from Staff where Cardin != 0 and Date between ? and ? order by Date"
        self.dbManager.cursor.execute(self.query, (self.date1, self.date2))
        self.rows = self.dbManager.cursor.fetchall()
        self.tableWidget.setRowCount(len(self.rows))
        
        self.tbrow = 0
        for i in self.rows:
            if i[6] == None:
                pr = ""
            else:
                pr = str(i[6])
            item = QtWidgets.QTableWidgetItem(str(i[0]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(self.tbrow, 0, item)
            item = QtWidgets.QTableWidgetItem(str(i[1]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(self.tbrow, 1, item)
            item = QtWidgets.QTableWidgetItem(format(i[2], ','))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(self.tbrow, 2, item)
            item = QtWidgets.QTableWidgetItem(str(i[3]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(self.tbrow, 3, item)
            item = QtWidgets.QTableWidgetItem(str(i[4]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(self.tbrow, 4, item)
            item = QtWidgets.QTableWidgetItem(str(i[5]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(self.tbrow, 5, item)
            item = QtWidgets.QTableWidgetItem(pr)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(self.tbrow, 6, item)
            self.tbrow += 1

        self.dbManager.close()
        
        
    def setupUi(self, Dialog_Card_Details):
        Dialog_Card_Details.setObjectName("Dialog_Card_Details")
        Dialog_Card_Details.resize(926, 847)
        self.dateEdit_1 = QtWidgets.QDateEdit(Dialog_Card_Details)
        self.dateEdit_1.setGeometry(QtCore.QRect(50, 770, 121, 41))
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
        self.dateEdit_2 = QtWidgets.QDateEdit(Dialog_Card_Details)
        self.dateEdit_2.setGeometry(QtCore.QRect(210, 770, 121, 41))
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
        
        self.dbManager = DBManager()
        self.label_11 = QtWidgets.QLabel(Dialog_Card_Details)
        self.label_11.setGeometry(QtCore.QRect(170, 779, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")

        self.label_calc = QtWidgets.QLabel(Dialog_Card_Details)
        self.label_calc.setGeometry(QtCore.QRect(320, 709, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_calc.setFont(font)
        self.label_calc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_calc.setObjectName("label_calc")

        self.btn_search = QtWidgets.QPushButton(Dialog_Card_Details, clicked = self.search_details)
        self.btn_search.setGeometry(QtCore.QRect(360, 760, 91, 61))
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

        self.dateEdit_3 = QtWidgets.QDateEdit(Dialog_Card_Details)
        self.dateEdit_3.setGeometry(QtCore.QRect(510, 770, 121, 41))
        self.dateEdit_3.setFocusPolicy(QtCore.Qt.NoFocus)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_3.setReadOnly(False)
        self.dateEdit_3.setCalendarPopup(True)
        self.dateEdit_3.setObjectName("dateEdit_3")

        self.btn_check = QtWidgets.QPushButton(Dialog_Card_Details, clicked = self.check_card)
        self.btn_check.setGeometry(QtCore.QRect(670, 760, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_check.setFont(font)
        self.btn_check.setAutoDefault(False)
        self.btn_check.setDefault(False)
        self.btn_check.setFlat(False)
        self.btn_check.setObjectName("btn_check")

        self.btn_cancel = QtWidgets.QPushButton(Dialog_Card_Details, clicked = self.cancel_card)
        self.btn_cancel.setGeometry(QtCore.QRect(830, 780, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setAutoDefault(False)
        self.btn_cancel.setDefault(False)
        self.btn_cancel.setFlat(False)
        self.btn_cancel.setObjectName("btn_cancel")
        
        current_date = datetime.date.today()
        # 10일 전 날짜
        ten_days_ago = current_date - datetime.timedelta(days=10)
        # 이번 달 1일 날짜
        first_day_of_month = current_date.replace(day=1)
        self.dateEdit_1.setDate(first_day_of_month)
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())
        self.dateEdit_3.setDate(QtCore.QDate.currentDate())
        self._today_button_1 = QtWidgets.QPushButton('&오늘', clicked=self.setToday_1)
        self.dateEdit_1.calendarWidget().layout().addWidget(self._today_button_1)
        self._today_button_2 = QtWidgets.QPushButton('&오늘', clicked=self.setToday_2)
        self.dateEdit_2.calendarWidget().layout().addWidget(self._today_button_2)
        self._today_button_3 = QtWidgets.QPushButton('&오늘', clicked=self.setToday_3)
        self.dateEdit_3.calendarWidget().layout().addWidget(self._today_button_3)
        
        self.tableWidget = QtWidgets.QTableWidget(Dialog_Card_Details)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 901, 691))
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
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setObjectName("tableWidget")
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
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 180)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(6, 130)
        
        self.dateEdit_1.wheelEvent = lambda event: None
        self.dateEdit_2.wheelEvent = lambda event: None
        self.dateEdit_3.wheelEvent = lambda event: None

        self.retranslateUi(Dialog_Card_Details)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Card_Details)

    def retranslateUi(self, Dialog_Card_Details):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Card_Details.setWindowTitle(_translate("Dialog_Card_Details", "Dialog"))
        self.label_11.setText(_translate("Dialog_Card_Details", "~"))
        self.label_calc.setText(_translate("Dialog_Card_Details", "합계: "))
        self.btn_search.setText(_translate("Dialog_Card_Details", "조회"))
        self.btn_check.setText(_translate("Dialog_Card_Details", "확인"))
        self.btn_cancel.setText(_translate("Dialog_Card_Details", "확인취소"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog_Card_Details", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog_Card_Details", "날짜"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog_Card_Details", "금액"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog_Card_Details", "승인번호"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog_Card_Details", "카드사"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Dialog_Card_Details", "이름"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Dialog_Card_Details", "확인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Card_Details = QtWidgets.QDialog()
    ui = Ui_Dialog_Card_Details()
    ui.setupUi(Dialog_Card_Details)
    Dialog_Card_Details.show()
    sys.exit(app.exec_())
