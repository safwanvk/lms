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

        self.show_category()
        self.show_author()
        self.show_publisher()

        self.show_category_combobox()
        self.show_author_combobox()
        self.show_publisher_combobox()

        
    def handle_buttons(self):
        self.pushButton.clicked.connect(self.day_to_day_tabs)
        self.pushButton_2.clicked.connect(self.books_tabs)
        self.pushButton_3.clicked.connect(self.users_tabs)
        self.pushButton_4.clicked.connect(self.settings_tab)

        self.pushButton_27.clicked.connect(self.add_new_category)
        self.pushButton_28.clicked.connect(self.add_new_author)
        self.pushButton_29.clicked.connect(self.add_new_publisher)

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
    def add_new_book(self, index):
        title = self.lineEdit_20.text()
        description = self.plainTextEdit_6.toPlainText()
        code = self.lineEdit_18.text()
        category = self.comboBox_20.itemData(index)
        author = self.comboBox_19.itemData(index)
        publisher = self.comboBox_18.itemData(index)
        price = self.lineEdit_19.text()
        
        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO books (title,code,description,category,author,publisher,price) VALUES (%s,%s,%s,%s,%s,%s,%s)
        ''' , (title,code,description,category,author,publisher,price))

        self.db.commit()
        self.statusBar().showMessage('New Book Addedd ')

        self.lineEdit_20.setText('')
        self.plainTextEdit_6.setPlainText('')
        self.lineEdit_18.setText('')
        self.comboBox_20.setCurrentIndex(0)
        self.comboBox_19.setCurrentIndex(0)
        self.comboBox_18.setCurrentIndex(0)
        self.lineEdit_19.setText('')

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
  
        category = self.lineEdit_55.text()

        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO categories (category) VALUES (%s)
        ''' , (category,))

        self.db.commit()
        self.statusBar().showMessage('New Category Addedd ')

        self.lineEdit_55.setText('')
        self.show_category()

    def show_category(self):
        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT category from categories ''')

        data = self.cur.fetchall()

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                    row_pos = self.tableWidget_2.rowCount()
                    self.tableWidget_2.insertRow(row_pos)


    def add_new_author(self):
  
        author = self.lineEdit_58.text()

        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO authors (author) VALUES (%s)
        ''' , (author,))

        self.db.commit()
        self.statusBar().showMessage('New Author Addedd ')

        self.lineEdit_58.setText('')
        self.show_author()

    def show_author(self):
        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT author from authors ''')

        data = self.cur.fetchall()

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                    row_pos = self.tableWidget_3.rowCount()
                    self.tableWidget_3.insertRow(row_pos)


    def add_new_publisher(self):

        publisher = self.lineEdit_59.text()

        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO publishers (publisher) VALUES (%s)
        ''' , (publisher,))

        self.db.commit()
        self.statusBar().showMessage('New Publisher Addedd ')

        self.lineEdit_59.setText('')
        self.show_publisher()

    def show_publisher(self):
        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT publisher from publishers ''')

        data = self.cur.fetchall()

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                    row_pos = self.tableWidget_4.rowCount()
                    self.tableWidget_4.insertRow(row_pos)

    def show_category_combobox(self):
        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT id, category from categories ''')

        data = self.cur.fetchall()

        if data:
            self.comboBox_3.clear()

            for i in data:
                self.comboBox_20.addItem(i[1], i[0])
                self.comboBox_3.addItem(i[1], i[0])

    def show_author_combobox(self):
        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT id, author from authors ''')

        data = self.cur.fetchall()

        if data:
            self.comboBox_4.clear()

            for i in data:
                self.comboBox_19.addItem(i[1], i[0])
                self.comboBox_4.addItem(i[1], i[0])

    def show_publisher_combobox(self):
        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT id, publisher from publishers ''')

        data = self.cur.fetchall()

        if data:
            self.comboBox_5.clear()

            for i in data:
                self.comboBox_18.addItem(i[1], i[0])
                self.comboBox_5.addItem(i[1], i[0])


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()