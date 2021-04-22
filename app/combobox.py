
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import run

def show_category_combobox(self):
    try:
        self.db = run.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT id, category from categories ''')

        data = self.cur.fetchall()
        self.cur.close()
        

        if data:
            self.comboBox_3.clear()

            for i in data:
                self.comboBox_20.addItem(i[1], i[0])
                self.comboBox_3.addItem(i[1], i[0])

    except Exception:
        self.statusBar().showMessage('Could not show category.')

def show_author_combobox(self):
    try:
        self.db = run.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT id, author from authors ''')

        data = self.cur.fetchall()
        self.cur.close()
        

        if data:
            self.comboBox_4.clear()

            for i in data:
                self.comboBox_19.addItem(i[1], i[0])
                self.comboBox_4.addItem(i[1], i[0])
    except Exception:
        self.statusBar().showMessage('Could not show author.')

def show_publisher_combobox(self):
    try:
        self.db = run.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT id, publisher from publishers ''')

        data = self.cur.fetchall()
        self.cur.close()
        

        if data:
            self.comboBox_5.clear()

            for i in data:
                self.comboBox_18.addItem(i[1], i[0])
                self.comboBox_5.addItem(i[1], i[0])
    except Exception:
        self.statusBar().showMessage('Could not show publisher.')

def show_title_combobox(self):
    try:
        self.db = run.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT id, title from books ''')

        data = self.cur.fetchall()
        self.cur.close()
        

        if data:
            self.comboBox_6.clear()
            self.comboBox_21.clear()

            for i in data:
                self.comboBox_6.addItem(i[1], i[0])
                self.comboBox_21.addItem(i[1], i[0])
    except Exception:
        self.statusBar().showMessage('Could not show title.')

def show_client_combobox(self):
    try:
        self.db = run.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT id, name from clients ''')

        data = self.cur.fetchall()
        self.cur.close()
        

        if data:
            self.comboBox_7.clear()
            self.comboBox_22.clear()

            for i in data:
                self.comboBox_7.addItem(i[1], i[0])
                self.comboBox_22.addItem(i[1], i[0])
    except Exception:
        self.statusBar().showMessage('Could not show client.')

def show_book_combobox(self):
    try:
        self.db = run.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT id, title from books ''')

        data = self.cur.fetchall()
        self.cur.close()
        

        if data:
            self.comboBox_21.clear()

            for i in data:
                self.comboBox_21.addItem(i[1], i[0])
    except Exception:
        self.statusBar().showMessage('Could not show book.')
