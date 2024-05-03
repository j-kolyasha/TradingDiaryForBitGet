from enums import *

class StatisticsCalculator():
    def calculateUserStatistics(self, orders : list, todayOrders : list):
        categorizeOrders = self.__categorizationOrders(orders)
        
        statistics = dict()
        statistics[TOTAL_TRADES] = self.__calculateCountOrders(categorizeOrders)
        statistics[AVERAGE_NET_PROFIT] = self.__calculateAverageNetProfit(categorizeOrders)
        statistics[TOTAL_PROFIT] = self.__calculateTotalProfit(categorizeOrders)
        statistics[PROFITABLE_TRADES] = self.__calculateCountProfitableOrders(categorizeOrders)
        statistics[LOSING_TRADES] = self.__calculateCountLosingOrders(categorizeOrders)
        statistics[PROFIT_CURRENT_DAY] = self.__calculateProfit(self.__categorizationOrders(todayOrders))
            
        return statistics

    def getChartPoints(self, orders : list):
        points = list()
        points.append(0)
        
        for order in orders:
            if len(points) <= 0:
                points.append(round(float(order[NET_PROFIT_INDEX]), 3))
                continue

            newPoint = round(float(points[len(points) - 1]) + float(order[NET_PROFIT_INDEX]), 3) 
            points.append(newPoint)
            
        return points
            

    def __calculateCountOrders(self, orders : list):
        return [len(orders[0]), len(orders[1]), len(orders[2])]

    def __calculateAverageNetProfit(self, categorizeOrders : list):        
        statistic = []
        
        for orders in categorizeOrders:
            numbers = []
            for order in orders:
                numbers.append(float(order[NET_PROFIT_INDEX]))
            
            statistic.append(self.__average(numbers))
            
        return statistic            
    
    def __calculateTotalProfit(self, orders : list):        
        profitL = 0
        profitS = 0
        
        for order in orders[1]:
            profitL += float(order[NET_PROFIT_INDEX])
        
        for order in orders[2]:
            profitS += float(order[NET_PROFIT_INDEX])
            
        return [round(profitL + profitS, 3), round(profitL, 3), round(profitS, 3)]  
    
    def __calculateCountProfitableOrders(self, orders : list):
        countL = 0
        countS = 0
        
        for order in orders[1]:
            if float(order[NET_PROFIT_INDEX]) > 0:
                countL += 1
        
        for order in orders[2]:
            if float(order[NET_PROFIT_INDEX]) > 0:
                countS += 1
        
        return [countL+countS, countL, countS]

    def __calculateCountLosingOrders(self, orders : list):
        countL = 0
        countS = 0
        
        for order in orders[1]:
            if float(order[NET_PROFIT_INDEX]) < 0:
                countL += 1
        
        for order in orders[2]:
            if float(order[NET_PROFIT_INDEX]) < 0:
                countS += 1
        
        return [countL+countS, countL, countS]

    def __calculateProfit(self, orders : list):        
        long = 0
        short = 0
        
        for order in orders[1]:
            long += float(order[NET_PROFIT_INDEX])
        for order in orders[2]:
            short += float(order[NET_PROFIT_INDEX])   
        
        return [round(long + short, 3), round(long, 3), round(short, 3)]
        
    def __categorizationOrders(self, orders : list):
        ordersL = []
        ordersS = []
        
        for order in orders:
            holdSide = order[HOLD_SIDE_INDEX]
            
            if holdSide == LONG:
                ordersL.append(order)
            else:
                ordersS.append(order)
                
        return [orders, ordersL, ordersS]
    
    def __average(self, numbers : list):
        numbersL = len(numbers)
        if numbersL <= 0:
            return 0
        
        return round(sum(numbers) / numbersL, 3)