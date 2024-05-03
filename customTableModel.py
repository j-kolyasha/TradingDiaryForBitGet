from PySide6 import QtCore
from PySide6.QtCore import Qt
from enums import *
import datetime
import time
from enums import *

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            column = index.column()
            if column == OPENING_DATE_INDEX or column == CLOSING_DATE_INDEX:
                return str(self.__dateConverterFromEpoch(self._data[index.row()][column]))
            
            return self._data[index.row()][column]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        try:
            return len(self._data[0])
        except:
            return 0
    
    def headerData(self, section: int, orientation: QtCore.Qt. Orientation, role: QtCore.Qt. ItemDataRole) :
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                0: f"{ID}",
                1: f"{TICKER}",
                2: f"{OPENING_DATE}",
                3: f"{CLOSING_DATE}",
                4: f"{HOLD_SIDE}",
                5: f"{OPEN_AVG_PRICE}",
                6: f"{CLOSE_AVG_PRICE}",
                7: f"{OPEN_TOTAL_POS}",
                8: f"{PNL}",
                9: f"{COMISSION_AND_FUNDING}",
                10: f"{NET_PROFIT}",
                }.get(section)
                
    def __dateConverterFromEpoch(self, date : str):
        return datetime.datetime.strptime(time.ctime(date), "%c")