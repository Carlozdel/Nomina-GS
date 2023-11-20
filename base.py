import sqlite3

connection =  sqlite3.connect('GS_DataBase')
cursorDB = connection.cursor()

def table_exists(tablename):
    cursorDB.execute('''SELECT COUNT(name) fROM SQLITE_MASTER where type = 'table' and name = '{}' '''.format(tablename))
    if cursorDB.fetchone()[0] == 1:
        return True
    else:
        cursorDB.execute('''CREATE TABLE Employee (EMPID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT) ''')
        return False
    

    table_exists(Employee)

