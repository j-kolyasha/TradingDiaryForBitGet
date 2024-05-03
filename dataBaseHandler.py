from dataBaseReader import DBReader
from dataBaseWriter import DBWriter
from enums import *
from datetime import date, datetime

import os
import time
import sqlite3 as sq

class DataBaseHandler():
    def __init__(self):    
        if os.path.exists("DataBase") == False:
            os.mkdir("DataBase")
        
        self._dbr = DBReader()
        self._dbw = DBWriter()
        
        self.__checkingExistenceOrCreateTables()
        
    def getUserAPI(self):
        return self._dbr.getUserAPI()
    
    def getLastOrder(self):
        return self._dbr.getLastOrder()

    def getOrders(self, condition = ''):
        return self._dbr.getOrders(condition)
    
    def addNewOrdersToDB(self, orders : list, startDate : str):
        self._dbw.addNewOrdersToDB(orders, startDate) 
        
    def addUserAPI(self, apiKey, apiSecretKey, passphrase):
        self.__clearDataUserTable()
        self._dbw.addUserAPI(apiKey, apiSecretKey, passphrase)
    
    def getOrdersOfCurrentDay(self):
        orders = self.getOrders()
        needOrders = list()
        
        currentDate = date.today()
        for order in orders:
            orderTime = order[CLOSING_DATE_INDEX]
            convertTime = str(datetime.strptime(time.ctime(float(orderTime)), "%c"))[0:10]
            if str(currentDate) == convertTime:
                needOrders.append(order)
                
        return needOrders
        
    def __clearDataUserTable(self):
        with sq.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute(f"""DELETE FROM {USER_DATA}""")
        
    def __checkingExistenceOrCreateTables(self):
        with sq.connect(DATABASE) as con:
            cur = con.cursor()
            
            cur.execute(f"""CREATE TABLE IF NOT EXISTS "{ORDERS}" (
                "{ID}" INTEGER,
                "{TICKER}" TEXT NOT NULL,
                "{OPENING_DATE}" REAL NOT NULL,
                "{CLOSING_DATE}" REAL,
                "{HOLD_SIDE}" TEXT NOT NULL,
                "{OPEN_AVG_PRICE}" REAL NOT NULL,
                "{CLOSE_AVG_PRICE}" REAL NOT NULL,
                "{OPEN_TOTAL_POS}" REAL NOT NULL,
                "{PNL}" REAL NOT NULL,
                "{COMISSION_AND_FUNDING}" REAL NOT NULL,
                "{NET_PROFIT}" REAL NOT NULL,
                PRIMARY KEY("{ID}")
                )""")
            
            cur.execute(f"""CREATE TABLE IF NOT EXISTS "{USER_DATA}" (
                "{API_KEY}" TEXT NOT NULL,
                "{SECRET_KEY}" TEXT NOT NULL,
                "{PASSPHRASE}" TEXT NOT NULL
                );""")
            
            