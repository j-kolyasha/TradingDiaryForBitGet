import sqlite3 as sq
from enums import *

class DBWriter():
    def addNewOrdersToDB(self, orders : list, startDate : str):
        with sq.connect(DATABASE) as con:
            cur = con.cursor()
            
            orders.reverse()

            for order in orders:
                utime = float(order['utime']) / 1000
                if startDate != '' and utime == float(startDate):
                    continue       
                
                comissionAndFunding = float(order['totalFunding']) + float(order['openFee']) + float(order['closeFee'])
                ctime = float(order['ctime']) / 1000
                cur.execute(f"""INSERT INTO {ORDERS} (ticker, openingDate, closingDate, holdSide, openAvgPrice, closeAvgPrice, openTotalPos, pnl, commissionAndFunding, netProfit)
                            VALUES ('{order['symbol']}', {ctime}, {utime}, 
                            '{order['holdSide']}', {order['openAvgPrice']}, {order['closeAvgPrice']},
                            {order['openTotalPos']}, {order['pnl']}, {comissionAndFunding},
                            {order['netProfit']})""")
                
    def addUserAPI(self, apiKey, apiSecretKey, passphrase):
        with sq.connect(DATABASE) as con:
            cur = con.cursor()
            
            cur.execute(f"""INSERT INTO {USER_DATA} ({API_KEY}, {SECRET_KEY}, {PASSPHRASE})
                            VALUES ('{apiKey}', '{apiSecretKey}', '{passphrase}')""")