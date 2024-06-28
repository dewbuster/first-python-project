import pyodbc
from win32 import win32print
import os
from PyQt5.QtWidgets import QMessageBox

class DBManager:
    def __init__(self):
        self.office = "Driver={SQL Server};Server=DESKTOP-58Q9HMK\SQLEXPRESS;Database=bakok;Trusted_Connection=yes;"
        self.home = "Driver={SQL Server};Server=DESKTOP-PN9M8RU\SQLEXPRESS;Database=bakok;Trusted_Connection=yes;"
        self.place = "office"
        if os.path.exists("C:/home/"):
            self.place = "home"
        
    def connect(self):
        if self.place == "office":
            try:
                self.conn = pyodbc.connect(self.office)
                self.cursor = self.conn.cursor()
            except:
                msg = QMessageBox()
                msg.setWindowTitle("오류")
                msg.setText("서버 연결 실패")
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec()
        else:
            try:
                self.conn = pyodbc.connect(self.home)
                self.cursor = self.conn.cursor()
            except:
                msg = QMessageBox()
                msg.setWindowTitle("오류")
                msg.setText("서버 연결 실패")
                msg.setIcon(QMessageBox.Critical)
                x = msg.exec()
    
    def close(self):
        self.conn.close()
        
class PrintManager:
    def __init__(self):
        self.place = "office"
        if os.path.exists("C:/home/"):
            self.place = "home"
    
    def setprinter(self):
        if self.place == "office":
            if win32print.GetDefaultPrinter() != "Samsung C48x Series (USB001)":
                win32print.SetDefaultPrinterW("Samsung C48x Series (USB001)")
                print(win32print.GetDefaultPrinter())
        else:
            return