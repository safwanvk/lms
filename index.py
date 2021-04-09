from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import mysql.connector
import sys
from PyQt5.uic import loadUiType

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="lms"
)

ui,_ = loadUiType('library.ui')

class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_buttons()
        self.tabWidget.tabBar().setVisible(False)
        
    def handle_buttons(self):
        self.pushButton.clicked.connect(self.day_to_day_tabs)
        self.pushButton_2.clicked.connect(self.books_tabs)
        self.pushButton_3.clicked.connect(self.users_tabs)
        self.pushButton_4.clicked.connect(self.settings_tab)

        self.pushButton_12.clicked.connect(self.add_new_book)

    #####Open Tabs######
    def day_to_day_tabs(self):
        self.tabWidget.setCurrentIndex(0)

    def books_tabs(self):
        self.tabWidget.setCurrentIndex(1)

    def users_tabs(self):
        self.tabWidget.setCurrentIndex(2)

    def settings_tab(self):
        self.tabWidget.setCurrentIndex(3)

    ######Day To Day#######

    ######Books############
    def add_new_book(self):
        self.cur = db.cursor()

        self.cur.execute(''' SELECT  * FROM books''')
        data = self.cur.fetchall()

        print(data)

    def edit_book(self):
        pass

    def delete_book(self):
        pass

    ######Users##########
    def add_new_user(self):
        pass

    def edit_user(self):
        pass

    def user_login(self):
        pass

    #####settings#######
    def add_new_category(self):
        pass

    def add_new_author(self):
        pass

    def add_new_publisher(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()