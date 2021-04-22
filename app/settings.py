
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import index

#####settings#######
def add_new_category(self):
    try:
        category = self.lineEdit_55.text()

        self.db = index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO categories (category) VALUES (?)
        ''' , (category,))

        self.db.commit()
        self.cur.close()
        self.statusBar().showMessage('New Category Addedd ')

        self.lineEdit_55.setText('')
        self.show_category()
    except Exception:
        self.statusBar().showMessage('Could not add category.')

def show_category(self):
    try:
        self.db =  index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT category from categories ''')

        data = self.cur.fetchall()
        self.cur.close()

        if data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                    row_pos = self.tableWidget_2.rowCount()
                    self.tableWidget_2.insertRow(row_pos)

    except Exception:
        self.statusBar().showMessage('Could not show category.')


def add_new_author(self):
    try:
        author = self.lineEdit_58.text()

        self.db =  index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO authors (author) VALUES (?)
        ''' , (author,))

        self.db.commit()
        self.cur.close()
        self.statusBar().showMessage('New Author Addedd ')

        self.lineEdit_58.setText('')
        self.show_author()
    except Exception as e:
        print(e)
        self.statusBar().showMessage('Could not add author.')

def show_author(self):
    try:
        self.db =  index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT author from authors ''')

        data = self.cur.fetchall()
        self.cur.close()

        if data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                    row_pos = self.tableWidget_3.rowCount()
                    self.tableWidget_3.insertRow(row_pos)
    except Exception:
        self.statusBar().showMessage('Could not show author.')


def add_new_publisher(self):
    try:
        publisher = self.lineEdit_59.text()

        self.db =  index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO publishers (publisher) VALUES (?)
        ''' , (publisher,))

        self.db.commit()
        self.cur.close()
        self.statusBar().showMessage('New Publisher Addedd ')

        self.lineEdit_59.setText('')
        self.show_publisher()
    except Exception:
        self.statusBar().showMessage('Could not add publisher.')

def show_publisher(self):
    try:
        self.db =  index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT publisher from publishers ''')

        data = self.cur.fetchall()
        self.cur.close()

        if data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                    row_pos = self.tableWidget_4.rowCount()
                    self.tableWidget_4.insertRow(row_pos)
    except Exception:
        self.statusBar().showMessage('Could not show publisher.')