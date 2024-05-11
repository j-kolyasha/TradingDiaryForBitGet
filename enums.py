# bitget api url
API_URL = 'https://api.bitget.com'

#headers
CONTENT_TYPE = 'Content-Type'
ACCESS_KEY = 'ACCESS-KEY'
ACCESS_SIGN = 'ACCESS-SIGN'
ACCESS_TIMESTAMP = 'ACCESS-TIMESTAMP'
ACCESS_PASSPHRASE = 'ACCESS-PASSPHRASE'
APPLICATION_JSON = 'application/json'
APPLICATION_JSON = 'application/json'

# params name
SYMBOL = 'symbol'
PRODUCT_TYPE = 'productType'
ID_LESS_THAN = 'idLessThan'
START_TIME = 'startTime'
END_TIME = 'endTime'
LIMIT = 'limit'

# params
USDT_FUTURES = 'USDT-FUTURES'

#requests path
HISTORYCAL_POSITION = '/api/v2/mix/position/history-position'
ACCOUNT_LIST = '/api/v2/mix/account/accounts'

#requests type
GET = 'GET'
POST = 'POST'
DELETE = 'DELETE' 

# database
DATABASE = 'DataBase/TradingDiary.db'
ORDERS = 'orders'
USER_DATA = 'userData'

# sql commands
AND = ' AND '
OR = ' OR '
LESS = '<'
MORE = '>'
EQUALLY = '='
BEETWEEN = '{} BETWEEN "{}" AND "{}"'
LIKE = '{} LIKE "%{}%"'
CONDITION = '{} {} "{}"'
WHERE = 'WHERE '

# table fills
ID = 'id'
TICKER = 'ticker'
OPENING_DATE = 'openingDate'
CLOSING_DATE = 'closingDate'
HOLD_SIDE = 'holdSide'
OPEN_AVG_PRICE = 'openAvgPrice'
CLOSE_AVG_PRICE = 'closeAvgPrice'
OPEN_TOTAL_POS = 'openTotalPos'
PNL = 'pnl'
COMISSION_AND_FUNDING = 'commissionAndFunding'
NET_PROFIT = 'netProfit'
API_KEY = 'apiKey'
SECRET_KEY = 'secretKey'
PASSPHRASE = 'passphrase'

# index fills in database (ordes)
ID_INDEX = 0
TICEKR_INDEX = 1
OPENING_DATE_INDEX = 2
CLOSING_DATE_INDEX = 3
HOLD_SIDE_INDEX = 4
OPEN_AVG_PRICE_INDEX = 5
CLOSE_AVG_PRICE_INDEX = 6
OPEN_TOTAL_POS_INDEX = 7
PNL_INDEX = 8
COMISSION_AND_FUNDING_INDEX = 9
NET_PROFIT_INDEX = 10

# holdSide
LONG = 'long'
SHORT = 'short'

# statistacs
TOTAL_TRADES = 'totalTrades'
AVERAGE_NET_PROFIT = 'averageNetProfit'
TOTAL_PROFIT = 'totalProfit'
PROFITABLE_TRADES = 'profitableTrades'
LOSING_TRADES = 'losingTrades'
PROFIT_CURRENT_DAY = 'profitCurrentDay'

# colors
from PySide6.QtGui import QColor
WHITE_COLOR = QColor(255, 255, 255)
GREEN_COLOR = QColor(0, 255, 0)
RED_COLOR = QColor(255, 0, 0)
GRAY_COLOR = QColor(121, 121, 121)
GRAY_TEXT_COLOR = QColor(175, 175, 175)

# selector
NO_METTER = 'no matter'
PROFIT = 'profit'
LOSS = 'loss'