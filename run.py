from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# import mysql.connector
import sys
from PyQt5.uic import loadUiType
import datetime
import os

import sqlite3 as sql

from app.book import *
from app.client import *
from app.combobox import *
from app.daily_operation import *
from app.settings import *
from app.user import *


os.system(resource_path('python3 connection.py'))
os.system(resource_path('python3 create_tables.py'))

import os, sys
# Translate asset paths to useable format for PyInstaller
def resource_path(relative_path):
  if hasattr(sys, '_MEIPASS'):
      return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath('.'), relative_path)




ui,_ = loadUiType(resource_path('library.ui'))
db = sql.connect(resource_path("library.db"))

class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_buttons()
        self.tabWidget.tabBar().setVisible(False)
        style = open('dark.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

        show_operations(self)

        show_books(self)

        show_category(self)
        show_author(self)
        show_publisher(self)

        show_client(self)

        show_title_combobox(self)

        show_category_combobox(self)
        show_author_combobox(self)
        show_publisher_combobox(self)

        show_client_combobox(self)
        show_book_combobox(self)

        
    def handle_buttons(self):
        self.pushButton.clicked.connect(self.day_to_day_tabs)
        self.pushButton_2.clicked.connect(self.books_tabs)
        self.pushButton_3.clicked.connect(self.users_tabs)
        self.pushButton_4.clicked.connect(self.settings_tab)
        self.pushButton_5.clicked.connect(self.client_tabs)

        self.pushButton_6.clicked.connect(day_operation)

        self.pushButton_27.clicked.connect(add_new_category)
        self.pushButton_28.clicked.connect(add_new_author)
        self.pushButton_29.clicked.connect(add_new_publisher)

        self.pushButton_12.clicked.connect(add_new_book)
        self.pushButton_11.clicked.connect(search_book)
        self.pushButton_7.clicked.connect(edit_book)
        self.pushButton_8.clicked.connect(delete_book)

        self.pushButton_14.clicked.connect(add_new_client)
        self.pushButton_16.clicked.connect(search_client)
        self.pushButton_26.clicked.connect(edit_client)
        self.pushButton_38.clicked.connect(delete_client)

        self.pushButton_18.clicked.connect(add_new_user)
        self.pushButton_20.clicked.connect(login)
        self.pushButton_37.clicked.connect(edit_user)


    #####Open Tabs######
    def day_to_day_tabs(self):
        self.tabWidget.setCurrentIndex(0)

    def books_tabs(self):
        self.tabWidget.setCurrentIndex(1)

    def users_tabs(self):
        self.tabWidget.setCurrentIndex(2)

    def client_tabs(self):
        self.tabWidget.setCurrentIndex(3)

    def settings_tab(self):
        self.tabWidget.setCurrentIndex(4)

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()