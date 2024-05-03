import sqlite3 as sq
from enums import *

class DBReader():
    def getOrders(self, condition : str = ''):
        with sq.connect(DATABASE) as con:
            cur = con.cursor()
            
            cur.execute(f"""SELECT * FROM {ORDERS} {condition}""")
            
            return cur.fetchall()
            
    def getUserAPI(self):
        with sq.connect(DATABASE) as con:
            cur = con.cursor()
            
            cur.execute(f"""SELECT * FROM {USER_DATA} DESC LIMIT 1""")
            
            result = cur.fetchall()
            if len(result) > 0:
                return result[0][0], result[0][1], result[0][2]
            
            return '', '', ''
        
    def getLastOrder(self):
        with sq.connect(DATABASE) as con:
            cur = con.cursor()
            
            cur.execute(f"""SELECT * FROM {ORDERS} ORDER BY id DESC LIMIT 1""")
            
            result = cur.fetchall()
            if len(result) > 0:
                return result[0]
            
            return ''