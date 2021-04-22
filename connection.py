import sqlite3 as sql

def db():
    try:
       db = sql.connect('library.db')
       print("Database created")
    except:
        print("failed to create database")
    finally:
        db.close()

if __name__ == "__main__":
    db()