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
        style = open('dark.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

        self.show_books()

        self.show_category()
        self.show_author()
        self.show_publisher()

        self.show_title_combobox()

        self.show_category_combobox()
        self.show_author_combobox()
        self.show_publisher_combobox()

        self.show_client_combobox()

        
    def handle_buttons(self):
        self.pushButton.clicked.connect(self.day_to_day_tabs)
        self.pushButton_2.clicked.connect(self.books_tabs)
        self.pushButton_3.clicked.connect(self.users_tabs)
        self.pushButton_4.clicked.connect(self.settings_tab)
        self.pushButton_5.clicked.connect(self.client_tabs)

        self.pushButton_27.clicked.connect(self.add_new_category)
        self.pushButton_28.clicked.connect(self.add_new_author)
        self.pushButton_29.clicked.connect(self.add_new_publisher)

        self.pushButton_12.clicked.connect(self.add_new_book)
        self.pushButton_11.clicked.connect(self.search_book)
        self.pushButton_7.clicked.connect(self.edit_book)
        self.pushButton_8.clicked.connect(self.delete_book)

        self.pushButton_14.clicked.connect(self.add_new_client)


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


    ######Day To Day#######

    ######Books############
    def add_new_book(self):
        title = self.lineEdit_20.text()
        description = self.plainTextEdit_6.toPlainText()
        code = self.lineEdit_18.text()
        category = self.comboBox_20.currentData()
        author = self.comboBox_19.currentData()
        publisher = self.comboBox_18.currentData()
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

        self.show_books()

    def show_books(self):
        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT b.code,b.title,a.author,p.publisher,c.category,b.price from books as b
            left join authors a on b.author=a.id left join publishers p on b.publisher=p.id
            left join categories c on b.category=c.id  ''')

        data = self.cur.fetchall()

        if data:
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_5.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                    row_pos = self.tableWidget_5.rowCount()
                    self.tableWidget_5.insertRow(row_pos)

    def search_book(self):
        id = self.comboBox_6.currentData()
        
        self.db = db
        self.cur = self.db.cursor()

        sql = ''' SELECT b.code,b.title,b.author,a.author as author_name,b.publisher,p.publisher as publisher_name,
            b.category,c.category as category_name,b.price,b.description from books as b
            left join authors a on b.author=a.id left join publishers p on b.publisher=p.id
            left join categories c on b.category=c.id where b.id=%s '''
        self.cur.execute(sql , [(id)])

        data = self.cur.fetchall()
 
        if data:
            self.lineEdit_5.setText(data[0][0])
            self.lineEdit_3.setText(data[0][1])
            self.comboBox_4.setCurrentText(data[0][3])
            self.comboBox_5.setCurrentText(data[0][5])
            self.comboBox_3.setCurrentText(data[0][7])
            self.lineEdit_6.setText(str(data[0][8]))
            self.plainTextEdit.setPlainText(data[0][9])
        else:
            self.statusBar().showMessage('No Book')


    def edit_book(self):

        id = self.comboBox_6.currentData()
        title = self.lineEdit_3.text()
        description = self.plainTextEdit.toPlainText()
        code = self.lineEdit_5.text()
        category = self.comboBox_3.currentData()
        author = self.comboBox_4.currentData()
        publisher = self.comboBox_5.currentData()
        price = self.lineEdit_6.text()

        
        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            update books set title=%s,code=%s,description=%s,category=%s,author=%s,publisher=%s,price=%s where id=%s
            ''' , (title,code,description,category,author,publisher,price,id))

        self.db.commit()
        self.statusBar().showMessage('Book Updated')

        self.comboBox_6.setCurrentIndex(0)
        self.lineEdit_3.setText('')
        self.plainTextEdit.setPlainText('')
        self.lineEdit_5.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_6.setText('')

        self.show_books()
        self.show_title_combobox()

    def delete_book(self):
        id = self.comboBox_6.currentData()

        warning = QMessageBox.warning(self , 'Delete Book' , "Are you sure you want to delete this book" , 
        QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            self.db = db
            self.cur = self.db.cursor()

            sql = ''' DELETE from books where id=%s '''
            self.cur.execute(sql , [(id)])
            self.db.commit()
            self.statusBar().showMessage('Book Deleted')

            self.comboBox_6.setCurrentIndex(0)
            self.lineEdit_3.setText('')
            self.plainTextEdit.setPlainText('')
            self.lineEdit_5.setText('')
            self.comboBox_3.setCurrentIndex(0)
            self.comboBox_4.setCurrentIndex(0)
            self.comboBox_5.setCurrentIndex(0)
            self.lineEdit_6.setText('')

            self.show_books()
            self.show_title_combobox()



    ######Users##########
    def add_new_user(self):
        pass

    def edit_user(self):
        pass

    def user_login(self):
        pass

    #######Client########
    def add_new_client(self):
        name = self.lineEdit_2.text()
        email = self.lineEdit_16.text()
        national_id = self.lineEdit_17.text()


        
        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO clients(name,email,national_id) VALUES (%s,%s,%s)
        ''' , (name,email,national_id))

        self.db.commit()
        self.statusBar().showMessage('New Client Addedd ')

        self.lineEdit_2.setText('')
        self.lineEdit_16.setText('')
        self.lineEdit_17.setText('')


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

    def show_title_combobox(self):
        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT id, title from books ''')

        data = self.cur.fetchall()

        if data:
            self.comboBox_6.clear()

            for i in data:
                self.comboBox_6.addItem(i[1], i[0])

    def show_client_combobox(self):
        self.db = db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT id, name from clients ''')

        data = self.cur.fetchall()

        if data:
            self.comboBox_7.clear()

            for i in data:
                self.comboBox_7.addItem(i[1], i[0])


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()