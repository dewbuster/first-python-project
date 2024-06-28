import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from yerim import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)

        file_menu = self.menuBar().addMenu("급여명세서")
        open_action = file_menu.addAction("명세서 입력")
        open_action.triggered.connect(self.open_payslip)
        deposit_action = file_menu.addAction("적금 관리")
        deposit_action.triggered.connect(self.open_deposit)

        
    def closeEvent(self, event):
        QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())