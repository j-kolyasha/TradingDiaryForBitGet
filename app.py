from PySide6.QtWidgets import QMainWindow, QDialog
from PySide6 import QtCharts
from PySide6.QtWidgets import QHeaderView
from PySide6.QtCore import QMargins, QDate
from mainWindowUI import Ui_MainWindow
from settingsWindowUI import Ui_Settings
from profileWindowUI import Ui_Profile

from dataBaseHandler import DataBaseHandler as dbh
from client import Client
from enums import *
from customTableModel import TableModel
from calendar import monthrange
import datetime
import time

from statisticsCalculator import StatisticsCalculator

class App(QMainWindow):    
    def __init__(self):
        super(App, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        
        self._dataBase = dbh()
        self._statisticsCalculator = StatisticsCalculator()
        
        self._ui.refreshButton.clicked.connect(self.__applyFilter)
        self._ui.settingsButton.clicked.connect(self.__openSettinsWindow)
        self._ui.profileButton.clicked.connect(self.__openProfileWindow)
        self.__updateViews(self._dataBase.getOrders())
        
        self.__startApp()
            
    def __startApp(self):
        apiKey, apiSecretKey, passphrase = self._dataBase.getUserAPI()
        if apiKey != '' and apiSecretKey != '' and passphrase != '':           
            self._client = Client(apiKey, apiSecretKey, passphrase)
            self.__updateData()
            self.__updateViews(self._dataBase.getOrders())
            self.__settingDefaultValues()
                
    def __settingDefaultValues(self):
        firstOrder = self._dataBase.getOrders(WHERE + CONDITION.format(ID, EQUALLY, 1))
        if len(firstOrder) > 0:
            firstOrder = firstOrder[0]
            startDate = firstOrder[CLOSING_DATE_INDEX]
            startDate = self.__dateConverterFromEpoch(startDate)
            self._ui.startDateEdit.setDate(QDate(startDate.year, startDate.month, startDate.day))
            
        finishDate = datetime.datetime.today()
        self._ui.finalDateEdit.setDate(QDate(finishDate.year, finishDate.month, finishDate.day))
    
    def __dateConverterFromEpoch(self, date : str):
        return datetime.datetime.strptime(time.ctime(date), "%c")
    
    def __updateData(self):
        try:
            order = self._dataBase.getLastOrder()
            startTime = int(float(order[CLOSING_DATE_INDEX]) * 1000) if len(order) > 0 else ''
            
            limit = 99
            if len(self._dataBase.getOrders()) <= 0:
                limit = 5
                
            params = self._client.getParams(productType=USDT_FUTURES, startTime=str(startTime), limit=str(limit))
            orders = self._client.request(GET, HISTORYCAL_POSITION, params)
        
            orders =  orders.json()['data']['list']
            if len(orders) >= 0:
                self._dataBase.addNewOrdersToDB(orders, startTime)
        except BaseException:
            print('чет не то в апи скорее всего')
            
    def __applyFilter(self):
        self.__updateData()
        filter = ''
        
        ticker = self._ui.tickerEdit.text()
        filter += WHERE + LIKE.format(TICKER, ticker)

        openingDate = self._ui.startDateEdit.text()
        d = openingDate.split('.')
        dt = datetime.datetime(int(d[2]), int(d[1]), int(d[0])) 
        startEpoch = dt.timestamp()
        
        finalDate = self._ui.finalDateEdit.text()
        d = finalDate.split('.')
        year = int(d[2])
        month = int(d[1])
        day = int(d[0])
        
        current_year = datetime.datetime.now().year     
        if day + 1 > monthrange(current_year, month)[1]:
            month += 1
            day = 0
        
        dt = datetime.datetime(year, month, day + 1) 
        finalEpoch = dt.timestamp()
            
        filter += AND + BEETWEEN.format(CLOSING_DATE, startEpoch, finalEpoch)
        
        direction = self._ui.directionSelector.currentText()
        direction = direction.lower()
        if direction != NO_METTER:
            filter += AND + CONDITION.format(HOLD_SIDE, EQUALLY, direction)
        
        profit = self._ui.profitSelector.currentText()
        profit = profit.lower()
        if profit == PROFIT:
            filter += AND + CONDITION.format(NET_PROFIT, MORE, 0) + OR + CONDITION.format(NET_PROFIT, EQUALLY, 0)
        if profit == LOSS:
            filter += AND + CONDITION.format(NET_PROFIT, LESS, 0)
        
        self.__updateViews(self._dataBase.getOrders(filter))    
            
    def __updateViews(self, trades : list):
        ordersOfCurrentDay = self._dataBase.getOrdersOfCurrentDay()        
        userStatistics = self._statisticsCalculator.calculateUserStatistics(trades, ordersOfCurrentDay)
        
        self._ui.totalTrades_total.setText(str(userStatistics[TOTAL_TRADES][0]))
        self._ui.totalTrades_long.setText(str(userStatistics[TOTAL_TRADES][1]))
        self._ui.totalTrades_short.setText(str(userStatistics[TOTAL_TRADES][2]))
        self._ui.avgNetProfit_total.setText(str(userStatistics[AVERAGE_NET_PROFIT][0]))
        self._ui.avgNetProfit_long.setText(str(userStatistics[AVERAGE_NET_PROFIT][1]))
        self._ui.avgNetProfit_short.setText(str(userStatistics[AVERAGE_NET_PROFIT][2]))
        self._ui.totalProfit_total.setText(str(userStatistics[TOTAL_PROFIT][0]))
        self._ui.totalProfit_long.setText(str(userStatistics[TOTAL_PROFIT][1]))
        self._ui.totalProfit_short.setText(str(userStatistics[TOTAL_PROFIT][2]))
        self._ui.profitTrades_total.setText(str(userStatistics[PROFITABLE_TRADES][0]))
        self._ui.profitTrades_long.setText(str(userStatistics[PROFITABLE_TRADES][1]))
        self._ui.profitTrades_short.setText(str(userStatistics[PROFITABLE_TRADES][2]))
        self._ui.losingTrades_total.setText(str(userStatistics[LOSING_TRADES][0]))
        self._ui.losingTrades_long.setText(str(userStatistics[LOSING_TRADES][1]))
        self._ui.losingTrades_short.setText(str(userStatistics[LOSING_TRADES][2]))
        self._ui.profitCurrentDay_total.setText(str(userStatistics[PROFIT_CURRENT_DAY][0]))
        self._ui.profitCurrentDay_long.setText(str(userStatistics[PROFIT_CURRENT_DAY][1]))
        self._ui.profitCurrentDay_short.setText(str(userStatistics[PROFIT_CURRENT_DAY][2]))
        
        series = QtCharts.QLineSeries()
        series.setPointsVisible(True)
        series.setMarkerSize(3)
        points = self._statisticsCalculator.getChartPoints(trades)
        for i in range(len(points)):
            series.append(float(i), float(points[i]))
        
        series.setColor(WHITE_COLOR)
        pointsLen = len(points)
        if len(points) > 0:
            if points[pointsLen - 1] >= 0:
                series.setColor(GREEN_COLOR)
            else:
                series.setColor(RED_COLOR)
            
        chart = QtCharts.QChart()
        chart.addSeries(series)       
        chart.setBackgroundVisible(False) 
        chart.setAnimationOptions(QtCharts.QChart.AnimationOption.SeriesAnimations)
        chart.legend().hide()
        
        margins = QMargins(-5, -5, -5, -5)
        chart.setMargins(margins)
        
        chart.createDefaultAxes()
        chart.axisX().setLabelFormat("%i")
        chart.axisX().setLabelsColor(WHITE_COLOR)
        chart.axisX().setGridLineColor(GRAY_COLOR)
        chart.axisY().setLabelsColor(WHITE_COLOR)
        chart.axisY().setGridLineColor(GRAY_COLOR)
        
        self._ui.netProfitGraph.setChart(chart)
        
        trades.reverse()
        self.model = TableModel(trades)
        self._ui.tradesView.setModel(self.model)
        self._ui.tradesView.horizontalHeader().resizeSection(0, 40)
        self._ui.tradesView.horizontalHeader().resizeSection(2, 140)
        self._ui.tradesView.horizontalHeader().resizeSection(3, 140)
        self._ui.tradesView.horizontalHeader().resizeSection(4, 100)
        self._ui.tradesView.horizontalHeader().resizeSection(8, 100)
        self._ui.tradesView.horizontalHeader().resizeSection(9, 138)
        self._ui.tradesView.horizontalHeader().resizeSection(10, 109)
        self._ui.tradesView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        
    def __openSettinsWindow(self):
        self.new_window = QDialog()
        self.ui_settingsWindow = Ui_Settings()
        self.ui_settingsWindow.setupUi(self.new_window)
        self.new_window.show()
        
        self.ui_settingsWindow.saveData.clicked.connect(self.__saveNewApiData)
    
    def __saveNewApiData(self):
        apiKey = self.ui_settingsWindow.apiKey.text()
        apiSecretKey = self.ui_settingsWindow.apiSecretKey.text()
        passphrase = self.ui_settingsWindow.passphrase.text()
        
        if apiKey != '' and apiSecretKey != '' and passphrase != '':      
            self.ui_settingsWindow.progress.setText('successfully')
            self.ui_settingsWindow.progress.setStyleSheet('color:rgb(0, 255, 0); font: 10pt "Courier New";')
            
            self._dataBase.addUserAPI(apiKey, apiSecretKey, passphrase)
            self.__startApp()
        else:
            self.ui_settingsWindow.progress.setText('failure')
            self.ui_settingsWindow.progress.setStyleSheet('color:rgb(255, 0, 0); font: 10pt "Courier New";')
            
    def __openProfileWindow(self):
        self.new_window = QDialog()
        self.ui_profileWindow = Ui_Profile()
        self.ui_profileWindow.setupUi(self.new_window)
        self.new_window.show()
        
        params = self._client.getParams(productType=USDT_FUTURES)
        data = self._client.request(GET, ACCOUNT_LIST, params)
        data =  data.json()['data'][0]
        print(data)
        
        prefix = ' USDT'
        self.ui_profileWindow.accountEquity.setText(str(round(float(data['accountEquity']), 3)) + prefix)
        self.ui_profileWindow.available.setText(str(round(float(data['available']), 3)) + prefix)
        self.ui_profileWindow.locked.setText(str(round(float(data['locked']), 3)) + prefix)