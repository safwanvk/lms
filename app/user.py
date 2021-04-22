import run
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


######Users##########
def add_new_user(self):

    try:
        user_name = self.lineEdit_9.text()
        email = self.lineEdit_25.text()
        password = self.lineEdit_26.text()
        password1 = self.lineEdit_27.text()

        if password == password1:
            self.db = run.db
            self.cur = self.db.cursor()

            self.cur.execute('''
                INSERT INTO users(username,email,password) VALUES (?,?,?)
            ''' , (user_name,email,password))

            self.db.commit()
            self.cur.close()
            self.statusBar().showMessage('New User Addedd')
            
            self.lineEdit_9.setText('')
            self.lineEdit_25.setText('')
            self.lineEdit_26.setText('')
            self.lineEdit_27.setText('')
        else:
            self.statusBar().showMessage('Please add a valid password twice')

    except Exception:
        self.statusBar().showMessage('Could not add new user.')

def login(self):
    try:
        user_name = self.lineEdit_34.text()
        password = self.lineEdit_35.text()

        
        self.db = run.db
        self.cur = self.db.cursor()

        sql = ''' SELECT * from users'''
        self.cur.execute(sql)

        data = self.cur.fetchall()
        self.cur.close()

        for i in data:
            if user_name == i[1] and password == i[3]:
                self.statusBar().showMessage('Valid Username & Password')

                self.lineEdit_40.setText(i[1])
                self.lineEdit_61.setText(i[2])
                self.lineEdit_82.setText(i[3])
            else:
                self.statusBar().showMessage('No Valid Username & Password')

    except Exception:
        self.statusBar().showMessage('Could not login.')

    

def edit_user(self):
    try:
        original_username = self.lineEdit_34.text()

        user_name = self.lineEdit_40.text()
        email = self.lineEdit_61.text()
        password = self.lineEdit_82.text()
        password1 = self.lineEdit_83.text()

        if password == password1:
        
            self.db = run.db
            self.cur = self.db.cursor()

            self.cur.execute('''
                update users set username=?,email=?,password=? where username=?
                ''' , (user_name,email,password,original_username))

            self.db.commit()
            self.cur.close()
            self.statusBar().showMessage('User Updated')

            self.lineEdit_34.setText('')
            self.lineEdit_35.setText('')
            self.lineEdit_40.setText('')
            self.lineEdit_61.setText('')
            self.lineEdit_82.setText('')
            self.lineEdit_83.setText('')
    except Exception:
        self.statusBar().showMessage('Could not login.')