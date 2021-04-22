import index
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

#######Client########
def add_new_client(self):
    try:
        name = self.lineEdit_2.text()
        email = self.lineEdit_16.text()
        national_id = self.lineEdit_17.text()


        
        self.db = index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO clients(name,email,national_id) VALUES (?,?,?)
        ''' , (name,email,national_id))

        self.db.commit()
        self.cur.close()
        self.statusBar().showMessage('New Client Addedd ')

        self.lineEdit_2.setText('')
        self.lineEdit_16.setText('')
        self.lineEdit_17.setText('')

        self.show_client()
    except Exception:
        self.statusBar().showMessage('Could not add client.')

def search_client(self):
    try:
        id = self.comboBox_7.currentData()
        
        self.db = index.db
        self.cur = self.db.cursor()

        sql = ''' SELECT name,email,national_id from clients where id=? '''
        self.cur.execute(sql , [(id)])

        data = self.cur.fetchall()
        self.cur.close()

        if data:
            self.lineEdit_31.setText(data[0][0])
            self.lineEdit_36.setText(data[0][1])
            self.lineEdit_56.setText(str(data[0][2]))
        else:
            self.statusBar().showMessage('No Client')
    except Exception:
        self.statusBar().showMessage('Could not search client.')

def show_client(self):
    try:
        self.db = index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT name,email,national_id from clients''')

        data = self.cur.fetchall()
        self.cur.close()

        if data:
            self.tableWidget_6.setRowCount(0)
            self.tableWidget_6.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget_6.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                    row_pos = self.tableWidget_6.rowCount()
                    self.tableWidget_6.insertRow(row_pos)
    except Exception:
        self.statusBar().showMessage('Could not show client.')

def edit_client(self):
    try:
        id = self.comboBox_7.currentData()

        name = self.lineEdit_31.text()
        email = self.lineEdit_36.text()
        national_id = self.lineEdit_56.text()

        
        self.db = index.db
        self.cur = self.db.cursor()

        print(name,email,type(national_id))

        self.cur.execute('''
            update clients set name=?,email=?,national_id=? where id=?
            ''' , (name,email,national_id,id))

        self.db.commit()
        self.cur.close()

        self.statusBar().showMessage('Client Updated')

        self.comboBox_7.setCurrentIndex(0)
        self.lineEdit_31.setText('')
        self.lineEdit_36.setText('')
        self.lineEdit_56.setText('')

        self.show_client_combobox()
        self.show_client()
    except Exception:
        self.statusBar().showMessage('Could not edit client.')

def delete_client(self):
    try:
        id = self.comboBox_7.currentData()

        warning = QMessageBox.warning(self , 'Delete Client' , "Are you sure you want to delete this client" , 
        QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes :
            self.db = db
            self.cur = self.db.cursor()

            sql = ''' DELETE from clients where id=? '''
            self.cur.execute(sql , [(id)])
            self.db.commit()
            self.cur.close()
            self.statusBar().showMessage('Client Deleted')

            self.comboBox_7.setCurrentIndex(0)
            self.lineEdit_31.setText('')
            self.lineEdit_36.setText('')
            self.lineEdit_56.setText('')

            self.show_client_combobox()
    except Exception:
        self.statusBar().showMessage('Could not delete client.')