import index
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

######Books############
def add_new_book(self):

    try:

        title = self.lineEdit_20.text()
        description = self.plainTextEdit_6.toPlainText()
        code = self.lineEdit_18.text()
        category = self.comboBox_20.currentData()
        author = self.comboBox_19.currentData()
        publisher = self.comboBox_18.currentData()
        price = self.lineEdit_19.text()

    
        self.db = index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO books (title,code,description,category,author,publisher,price) VALUES (?,?,?,?,?,?,?)
        ''' , (title,code,description,category,author,publisher,price))

        self.db.commit()
        self.cur.close()
        self.statusBar().showMessage('New Book Addedd ')

        self.lineEdit_20.setText('')
        self.plainTextEdit_6.setPlainText('')
        self.lineEdit_18.setText('')
        self.comboBox_20.setCurrentIndex(0)
        self.comboBox_19.setCurrentIndex(0)
        self.comboBox_18.setCurrentIndex(0)
        self.lineEdit_19.setText('')

        self.show_books()
        self.show_title_combobox()

    except Exception:
        self.statusBar().showMessage('Could not add book.')


def show_books(self):
    try:
        self.db = index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT b.code,b.title,a.author,p.publisher,c.category,b.price from books as b
            left join authors a on b.author=a.id left join publishers p on b.publisher=p.id
            left join categories c on b.category=c.id  ''')

        data = self.cur.fetchall()
        self.cur.close()

        if data:
            self.tableWidget_5.setRowCount(0)
            self.tableWidget_5.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_5.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                    row_pos = self.tableWidget_5.rowCount()
                    self.tableWidget_5.insertRow(row_pos)

    except Exception as e:
        print(e)
        self.statusBar().showMessage('Could not show book.')

def search_book(self):
    try:
        id = self.comboBox_6.currentData()
        
        self.db = index.db
        self.cur = self.db.cursor()

        sql = ''' SELECT b.code,b.title,b.author,a.author as author_name,b.publisher,p.publisher as publisher_name,
            b.category,c.category as category_name,b.price,b.description from books as b
            left join authors a on b.author=a.id left join publishers p on b.publisher=p.id
            left join categories c on b.category=c.id where b.id=? '''
        self.cur.execute(sql , [(id)])

        data = self.cur.fetchall()
        self.cur.close()

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

    except Exception:
        self.statusBar().showMessage('Could not search book.')


def edit_book(self):
    try:
        id = self.comboBox_6.currentData()
        title = self.lineEdit_3.text()
        description = self.plainTextEdit.toPlainText()
        code = self.lineEdit_5.text()
        category = self.comboBox_3.currentData()
        author = self.comboBox_4.currentData()
        publisher = self.comboBox_5.currentData()
        price = self.lineEdit_6.text()

        
        self.db = index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            update books set title=?,code=?,description=?,category=?,author=?,publisher=?,price=? where id=?
            ''' , (title,code,description,category,author,publisher,price,id))

        self.db.commit()
        self.cur.close()
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
    except Exception:
        self.statusBar().showMessage('Could not edit book.')

def delete_book(self):
    try:
        id = self.comboBox_6.currentData()

        warning = QMessageBox.warning(self , 'Delete Book' , "Are you sure you want to delete this book" , 
        QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :

            self.db = index.db
            self.cur = self.db.cursor()

            sql = ''' DELETE from books where id=? '''
            self.cur.execute(sql , [(id)])
            self.db.commit()
            self.cur.close()
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
    except Exception:
        self.statusBar().showMessage('Could not delete book.')


