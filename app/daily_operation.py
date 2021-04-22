import datetime
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import index


######Day To Day#######
def day_operation(self):
    try:

        client_id = self.comboBox_22.currentData()
        book_id = self.comboBox_21.currentData()
        type = self.comboBox.currentText()
        day = self.comboBox_2.currentIndex() + 1
        today =  datetime.date.today()
        to_date = today + datetime.timedelta(days=day)
        
        self.db = index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO day_operations(client_id,book_id,type,days,date,to_date) VALUES (?,?,?,?,?,?)
        ''' , (client_id,book_id,type,day,today,to_date))

        self.db.commit()
        self.cur.close()
        self.statusBar().showMessage('New operation Addedd')

        self.comboBox_22.setCurrentIndex(0)
        self.comboBox_21.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)

        self.show_operations()
    except Exception:
        self.statusBar().showMessage('Could not added operation.')


def show_operations(self):
    try:
        self.db = index.db
        self.cur = self.db.cursor()

        self.cur.execute('''
            SELECT c.name,b.title,d.type,d.days,d.date,d.to_date from day_operations as d
            left join clients c on d.client_id=c.id left join books b on d.book_id=b.id
            ''')

        data = self.cur.fetchall()
        self.cur.close()

        if data:
            self.tableWidget.setRowCount(0)
            self.tableWidget.insertRow(0)

            for row, form in enumerate(data):
                for column, item in enumerate(form):
                    self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                    row_pos = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row_pos)

    except Exception:
        self.statusBar().showMessage('Could not show operation.')