from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from dbmanager import DBManager
from filemanager import FileManager
import datetime

class Ui_Dialog_Deposit(object):

    def rBtn_clicked(self):
        if self.rBtn_1.isChecked():
            self.sBox_deposit.setEnabled(True)
        else:
            self.sBox_deposit.setEnabled(False)
    
    def set_position(self):
        if self.cBox_name.currentText() == "":
            pass
        else:
            self.name = self.cBox_name.currentText()

            self.lineEdit_position.setText("")
            self.sBox_deposit.setValue(0)
            self.rBtn_2.setChecked(True)
            self.sBox_deposit.setEnabled(False)

            self.dbManager.connect()
            self.query = "SELECT * FROM Deposit WHERE Name = ?"
            rows = self.dbManager.cursor.execute(self.query, (self.name)).fetchall()

            for i in rows:
                self.lineEdit_position.setText(i[1])
                if i[2] == 0:
                    self.sBox_deposit.setValue(0)
                    self.rBtn_2.setChecked(True)
                    self.sBox_deposit.setEnabled(False)
                else:
                    today = datetime.date.today()
                    xx = i[3].split('-')
                    passed = i[2] + ((int(today.year) - int(xx[0])) * 12 + (int(today.month) - int(xx[1])))
                    self.rBtn_1.setChecked(True)
                    self.sBox_deposit.setEnabled(True)
                    self.sBox_deposit.setValue(passed)
                
            self.dbManager.conn.commit()


    def insert_deposit(self):
        if self.cBox_name.currentText() == "":
            msg = QMessageBox()
            msg.setWindowTitle("오류")
            msg.setText("이름을 선택하세요")
            msg.setIcon(QMessageBox.Critical)
            x = msg.exec()
        else:
            self.date = str(datetime.date.today()) 
            self.name = self.cBox_name.currentText()
            self.position = self.lineEdit_position.text()
            if self.rBtn_1.isChecked():
                self.deposit = self.sBox_deposit.value()
            else:
                self.deposit = 0

            self.dbManager.connect()

            self.query = "IF EXISTS (SELECT * FROM Deposit WHERE Name = ?) BEGIN UPDATE Deposit SET Position = ?, Deposit = ?, Date = ? WHERE Name = ? END ELSE BEGIN INSERT INTO Deposit (Name, Position, Deposit, Date) VALUES(?,?,?,?) END"
            self.dbManager.cursor.execute(self.query, (self.name, self.position, self.deposit, self.date, self.name, self.name, self.position, self.deposit, self.date))
            self.dbManager.conn.commit()
            msg = QMessageBox()
            msg.setWindowTitle("입력완료")
            msg.setText("입력 되었습니다.")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec()
            self.cBox_name.setCurrentIndex(-1)
            self.lineEdit_position.setText("")
            self.sBox_deposit.setValue(0)
            self.rBtn_2.setChecked(True)
            self.sBox_deposit.setEnabled(False)

    def setupUi(self, Dialog_Deposit):
        Dialog_Deposit.setObjectName("Dialog_Deposit")
        Dialog_Deposit.resize(609, 264)
        Dialog_Deposit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.fManager = FileManager()
        self.dbManager = DBManager()
        self.cBox_name = QtWidgets.QComboBox(Dialog_Deposit)
        self.cBox_name.setGeometry(QtCore.QRect(80, 60, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cBox_name.setFont(font)
        self.cBox_name.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cBox_name.setEditable(False)
        self.cBox_name.setModelColumn(0)
        self.cBox_name.addItems(self.fManager.payslip)
        self.cBox_name.setCurrentIndex(-1)
        self.cBox_name.setObjectName("cBox_name")
        
        self.label_2 = QtWidgets.QLabel(Dialog_Deposit)
        self.label_2.setGeometry(QtCore.QRect(220, 60, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_info = QtWidgets.QLabel(Dialog_Deposit)
        self.label_info.setGeometry(QtCore.QRect(90, 210, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_info.setFont(font)
        self.label_info.setObjectName("label_info")

        self.btn_insert = QtWidgets.QPushButton(Dialog_Deposit, clicked=self.insert_deposit)
        self.btn_insert.setGeometry(QtCore.QRect(430, 90, 111, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_insert.setFont(font)
        self.btn_insert.setAutoDefault(False)
        self.btn_insert.setDefault(False)
        self.btn_insert.setFlat(False)
        self.btn_insert.setObjectName("btn_insert")
        self.lineEdit_position = QtWidgets.QLineEdit(Dialog_Deposit)
        self.lineEdit_position.setGeometry(QtCore.QRect(280, 60, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_position.setFont(font)
        self.lineEdit_position.setObjectName("lineEdit_position")
        self.groupBox = QtWidgets.QGroupBox(Dialog_Deposit)
        self.groupBox.setGeometry(QtCore.QRect(70, 122, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.groupBox.setObjectName("groupBox")
        self.rBtn_1 = QtWidgets.QRadioButton(self.groupBox, clicked=self.rBtn_clicked)
        self.rBtn_1.setGeometry(QtCore.QRect(30, 34, 90, 16))
        self.rBtn_1.setChecked(False)
        self.rBtn_1.setObjectName("rBtn_1")
        self.rBtn_2 = QtWidgets.QRadioButton(self.groupBox, clicked=self.rBtn_clicked)
        self.rBtn_2.setGeometry(QtCore.QRect(210, 34, 90, 16))
        self.rBtn_2.setChecked(True)
        self.rBtn_2.setObjectName("rBtn_2")
        self.sBox_deposit = QtWidgets.QSpinBox(self.groupBox)
        self.sBox_deposit.setEnabled(False)
        self.sBox_deposit.setGeometry(QtCore.QRect(101, 28, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sBox_deposit.setFont(font)
        self.sBox_deposit.setMinimum(1)
        self.sBox_deposit.setMaximum(200)
        self.sBox_deposit.setObjectName("sBox_deposit")

        self.cBox_name.currentIndexChanged['int'].connect(self.set_position)

        self.retranslateUi(Dialog_Deposit)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Deposit)

    def retranslateUi(self, Dialog_Deposit):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Deposit.setWindowTitle(_translate("Dialog_Deposit", "Dialog"))
        self.label_2.setText(_translate("Dialog_Deposit", "직급:"))
        self.label_info.setText(_translate("Dialog_Deposit", "*"))
        self.btn_insert.setText(_translate("Dialog_Deposit", "입력"))
        self.groupBox.setTitle(_translate("Dialog_Deposit", "적금"))
        self.rBtn_1.setText(_translate("Dialog_Deposit", "횟수:"))
        self.rBtn_2.setText(_translate("Dialog_Deposit", "없음"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog_Deposit = QtWidgets.QDialog()
    ui = Ui_Dialog_Deposit()
    ui.setupUi(Dialog_Deposit)
    Dialog_Deposit.show()
    sys.exit(app.exec_())
