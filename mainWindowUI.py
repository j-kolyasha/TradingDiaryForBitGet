# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDateEdit, QDateTimeEdit, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1239, 689)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1239, 689))
        MainWindow.setMaximumSize(QSize(1239, 689))
        icon = QIcon()
        icon.addFile(u":/icons/Resources/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #444446;")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 1218, 671))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_46 = QLabel(self.layoutWidget)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"color: rgb(175, 175, 175);\n"
"font: 20pt \"Courier New\";\n"
"border: none;\n"
"padding-bottom: 5px;")

        self.horizontalLayout_12.addWidget(self.label_46)

        self.profileButton = QPushButton(self.layoutWidget)
        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setMinimumSize(QSize(0, 0))
        self.profileButton.setMaximumSize(QSize(30, 30))
        self.profileButton.setStyleSheet(u"QPushButton\n"
"{\n"
"color: rgb(175, 175, 175);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);\n"
"}\n"
"QPushButton:hover \n"
"{\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed \n"
"{\n"
"font: bold 10pt \"Courier New\";\n"
"border: 1px solid rgb(0, 255, 0);\n"
"color: rgb(0, 255, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Resources/profile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profileButton.setIcon(icon1)
        self.profileButton.setIconSize(QSize(24, 24))
        self.profileButton.setAutoDefault(False)

        self.horizontalLayout_12.addWidget(self.profileButton)

        self.settingsButton = QPushButton(self.layoutWidget)
        self.settingsButton.setObjectName(u"settingsButton")
        self.settingsButton.setMinimumSize(QSize(0, 0))
        self.settingsButton.setMaximumSize(QSize(30, 30))
        self.settingsButton.setStyleSheet(u"QPushButton\n"
"{\n"
"color: rgb(175, 175, 175);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);\n"
"}\n"
"QPushButton:hover \n"
"{\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed \n"
"{\n"
"font: bold 10pt \"Courier New\";\n"
"border: 1px solid rgb(0, 255, 0);\n"
"color: rgb(0, 255, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Resources/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsButton.setIcon(icon2)
        self.settingsButton.setIconSize(QSize(24, 24))
        self.settingsButton.setAutoDefault(False)

        self.horizontalLayout_12.addWidget(self.settingsButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.netProfitGraph = QChartView(self.layoutWidget)
        self.netProfitGraph.setObjectName(u"netProfitGraph")
        self.netProfitGraph.setStyleSheet(u"border: 1px solid rgb(121, 121, 121);\n"
"color: rgb(255, 255, 255);")
        self.netProfitGraph.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.netProfitGraph.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_7.addWidget(self.netProfitGraph)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_45 = QLabel(self.layoutWidget)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"color:rgb(175, 175, 175);\n"
"font: 8pt \"Courier New\";\n"
"border: none")
        self.label_45.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_6.addWidget(self.label_45)

        self.tickerEdit = QLineEdit(self.layoutWidget)
        self.tickerEdit.setObjectName(u"tickerEdit")
        self.tickerEdit.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")

        self.verticalLayout_6.addWidget(self.tickerEdit)


        self.horizontalLayout_11.addLayout(self.verticalLayout_6)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(120, 0))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"color:rgb(175, 175, 175);\n"
"font: 8pt \"Courier New\";\n"
"border: none;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.startDateEdit = QDateEdit(self.layoutWidget)
        self.startDateEdit.setObjectName(u"startDateEdit")
        self.startDateEdit.setMinimumSize(QSize(120, 0))
        self.startDateEdit.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.startDateEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.startDateEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.startDateEdit.setKeyboardTracking(True)
        self.startDateEdit.setProperty("showGroupSeparator", False)
        self.startDateEdit.setCurrentSection(QDateTimeEdit.Section.DaySection)

        self.verticalLayout_2.addWidget(self.startDateEdit)


        self.horizontalLayout_11.addLayout(self.verticalLayout_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_44 = QLabel(self.layoutWidget)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(120, 0))
        self.label_44.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_44.setStyleSheet(u"color:rgb(175, 175, 175);\n"
"font: 8pt \"Courier New\";\n"
"border: none;")
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_44)

        self.finalDateEdit = QDateEdit(self.layoutWidget)
        self.finalDateEdit.setObjectName(u"finalDateEdit")
        self.finalDateEdit.setMinimumSize(QSize(120, 0))
        self.finalDateEdit.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.finalDateEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.finalDateEdit.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.finalDateEdit.setKeyboardTracking(True)
        self.finalDateEdit.setProperty("showGroupSeparator", False)
        self.finalDateEdit.setCurrentSection(QDateTimeEdit.Section.DaySection)

        self.verticalLayout_5.addWidget(self.finalDateEdit)


        self.horizontalLayout_11.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(120, 0))
        self.label_2.setStyleSheet(u"color:rgb(175, 175, 175);\n"
"font: 8pt \"Courier New\";\n"
"border: none")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.directionSelector = QComboBox(self.layoutWidget)
        self.directionSelector.addItem("")
        self.directionSelector.addItem("")
        self.directionSelector.addItem("")
        self.directionSelector.setObjectName(u"directionSelector")
        self.directionSelector.setMinimumSize(QSize(120, 0))
        self.directionSelector.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.directionSelector.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.directionSelector.setEditable(False)
        self.directionSelector.setModelColumn(0)

        self.verticalLayout_3.addWidget(self.directionSelector)


        self.horizontalLayout_11.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setStyleSheet(u"color:rgb(175, 175, 175);\n"
"font: 8pt \"Courier New\";\n"
"border: none")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.profitSelector = QComboBox(self.layoutWidget)
        self.profitSelector.addItem("")
        self.profitSelector.addItem("")
        self.profitSelector.addItem("")
        self.profitSelector.setObjectName(u"profitSelector")
        self.profitSelector.setMinimumSize(QSize(120, 0))
        self.profitSelector.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.profitSelector.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.profitSelector.setEditable(False)
        self.profitSelector.setModelColumn(0)

        self.verticalLayout_4.addWidget(self.profitSelector)


        self.horizontalLayout_11.addLayout(self.verticalLayout_4)

        self.refreshButton = QPushButton(self.layoutWidget)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setMinimumSize(QSize(42, 42))
        self.refreshButton.setMaximumSize(QSize(42, 42))
        self.refreshButton.setStyleSheet(u"QPushButton\n"
"{\n"
"color: rgb(175, 175, 175);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);\n"
"}\n"
"QPushButton:hover \n"
"{\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed \n"
"{\n"
"font: bold 10pt \"Courier New\";\n"
"border: 1px solid rgb(0, 255, 0);\n"
"color: rgb(0, 255, 0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Resources/reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon3)
        self.refreshButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.refreshButton)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)


        self.horizontalLayout_13.addLayout(self.verticalLayout_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 0))
        self.label_4.setMaximumSize(QSize(200, 16777215))
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet(u"color: rgb(175, 175, 175);\n"
"font: 14pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setMaximumSize(QSize(100, 16777215))
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setStyleSheet(u"color: rgb(175, 175, 175);\n"
"font: 14pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))
        self.label_6.setMaximumSize(QSize(100, 16777215))
        self.label_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_6.setStyleSheet(u"color: rgb(175, 175, 175);\n"
"font: 14pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_6)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 0))
        self.label_7.setMaximumSize(QSize(100, 16777215))
        self.label_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_7.setStyleSheet(u"color: rgb(175, 175, 175);\n"
"font: 14pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_7)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(200, 0))
        self.label_8.setMaximumSize(QSize(200, 16777215))
        self.label_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_8.setStyleSheet(u"color: rgb(175, 175, 175);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.label_8)

        self.totalTrades_total = QLabel(self.layoutWidget)
        self.totalTrades_total.setObjectName(u"totalTrades_total")
        self.totalTrades_total.setMinimumSize(QSize(100, 0))
        self.totalTrades_total.setMaximumSize(QSize(100, 16777215))
        self.totalTrades_total.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.totalTrades_total.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.totalTrades_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.totalTrades_total)

        self.totalTrades_long = QLabel(self.layoutWidget)
        self.totalTrades_long.setObjectName(u"totalTrades_long")
        self.totalTrades_long.setMinimumSize(QSize(100, 0))
        self.totalTrades_long.setMaximumSize(QSize(100, 16777215))
        self.totalTrades_long.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.totalTrades_long.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.totalTrades_long.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.totalTrades_long)

        self.totalTrades_short = QLabel(self.layoutWidget)
        self.totalTrades_short.setObjectName(u"totalTrades_short")
        self.totalTrades_short.setMinimumSize(QSize(100, 0))
        self.totalTrades_short.setMaximumSize(QSize(100, 16777215))
        self.totalTrades_short.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.totalTrades_short.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.totalTrades_short.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.totalTrades_short)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(200, 0))
        self.label_12.setMaximumSize(QSize(200, 16777215))
        self.label_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_12.setStyleSheet(u"color: rgb(175, 175, 175);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_12)

        self.avgNetProfit_total = QLabel(self.layoutWidget)
        self.avgNetProfit_total.setObjectName(u"avgNetProfit_total")
        self.avgNetProfit_total.setMinimumSize(QSize(100, 0))
        self.avgNetProfit_total.setMaximumSize(QSize(100, 16777215))
        self.avgNetProfit_total.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.avgNetProfit_total.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.avgNetProfit_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.avgNetProfit_total)

        self.avgNetProfit_long = QLabel(self.layoutWidget)
        self.avgNetProfit_long.setObjectName(u"avgNetProfit_long")
        self.avgNetProfit_long.setMinimumSize(QSize(100, 0))
        self.avgNetProfit_long.setMaximumSize(QSize(100, 16777215))
        self.avgNetProfit_long.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.avgNetProfit_long.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.avgNetProfit_long.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.avgNetProfit_long)

        self.avgNetProfit_short = QLabel(self.layoutWidget)
        self.avgNetProfit_short.setObjectName(u"avgNetProfit_short")
        self.avgNetProfit_short.setMinimumSize(QSize(100, 0))
        self.avgNetProfit_short.setMaximumSize(QSize(100, 16777215))
        self.avgNetProfit_short.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.avgNetProfit_short.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.avgNetProfit_short.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.avgNetProfit_short)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_18 = QLabel(self.layoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(200, 0))
        self.label_18.setMaximumSize(QSize(200, 16777215))
        self.label_18.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_18.setStyleSheet(u"color: rgb(175, 175, 175);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_18)

        self.totalProfit_total = QLabel(self.layoutWidget)
        self.totalProfit_total.setObjectName(u"totalProfit_total")
        self.totalProfit_total.setMinimumSize(QSize(100, 0))
        self.totalProfit_total.setMaximumSize(QSize(100, 16777215))
        self.totalProfit_total.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.totalProfit_total.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.totalProfit_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.totalProfit_total)

        self.totalProfit_long = QLabel(self.layoutWidget)
        self.totalProfit_long.setObjectName(u"totalProfit_long")
        self.totalProfit_long.setMinimumSize(QSize(100, 0))
        self.totalProfit_long.setMaximumSize(QSize(100, 16777215))
        self.totalProfit_long.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.totalProfit_long.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.totalProfit_long.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.totalProfit_long)

        self.totalProfit_short = QLabel(self.layoutWidget)
        self.totalProfit_short.setObjectName(u"totalProfit_short")
        self.totalProfit_short.setMinimumSize(QSize(100, 0))
        self.totalProfit_short.setMaximumSize(QSize(100, 16777215))
        self.totalProfit_short.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.totalProfit_short.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.totalProfit_short.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.totalProfit_short)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_16 = QLabel(self.layoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(200, 0))
        self.label_16.setMaximumSize(QSize(200, 16777215))
        self.label_16.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_16.setStyleSheet(u"color: rgb(175, 175, 175);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label_16)

        self.profitTrades_total = QLabel(self.layoutWidget)
        self.profitTrades_total.setObjectName(u"profitTrades_total")
        self.profitTrades_total.setMinimumSize(QSize(100, 0))
        self.profitTrades_total.setMaximumSize(QSize(100, 16777215))
        self.profitTrades_total.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.profitTrades_total.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.profitTrades_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.profitTrades_total)

        self.profitTrades_long = QLabel(self.layoutWidget)
        self.profitTrades_long.setObjectName(u"profitTrades_long")
        self.profitTrades_long.setMinimumSize(QSize(100, 0))
        self.profitTrades_long.setMaximumSize(QSize(100, 16777215))
        self.profitTrades_long.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.profitTrades_long.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.profitTrades_long.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.profitTrades_long)

        self.profitTrades_short = QLabel(self.layoutWidget)
        self.profitTrades_short.setObjectName(u"profitTrades_short")
        self.profitTrades_short.setMinimumSize(QSize(100, 0))
        self.profitTrades_short.setMaximumSize(QSize(100, 16777215))
        self.profitTrades_short.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.profitTrades_short.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.profitTrades_short.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.profitTrades_short)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_28 = QLabel(self.layoutWidget)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(200, 0))
        self.label_28.setMaximumSize(QSize(200, 16777215))
        self.label_28.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_28.setStyleSheet(u"color: rgb(175, 175, 175);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_28)

        self.losingTrades_total = QLabel(self.layoutWidget)
        self.losingTrades_total.setObjectName(u"losingTrades_total")
        self.losingTrades_total.setMinimumSize(QSize(100, 0))
        self.losingTrades_total.setMaximumSize(QSize(100, 16777215))
        self.losingTrades_total.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.losingTrades_total.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.losingTrades_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.losingTrades_total)

        self.losingTrades_long = QLabel(self.layoutWidget)
        self.losingTrades_long.setObjectName(u"losingTrades_long")
        self.losingTrades_long.setMinimumSize(QSize(100, 0))
        self.losingTrades_long.setMaximumSize(QSize(100, 16777215))
        self.losingTrades_long.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.losingTrades_long.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.losingTrades_long.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.losingTrades_long)

        self.losingTrades_short = QLabel(self.layoutWidget)
        self.losingTrades_short.setObjectName(u"losingTrades_short")
        self.losingTrades_short.setMinimumSize(QSize(100, 0))
        self.losingTrades_short.setMaximumSize(QSize(100, 16777215))
        self.losingTrades_short.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.losingTrades_short.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.losingTrades_short.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.losingTrades_short)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_24 = QLabel(self.layoutWidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(200, 0))
        self.label_24.setMaximumSize(QSize(200, 16777215))
        self.label_24.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_24.setStyleSheet(u"color: rgb(175, 175, 175);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_24)

        self.profitCurrentDay_total = QLabel(self.layoutWidget)
        self.profitCurrentDay_total.setObjectName(u"profitCurrentDay_total")
        self.profitCurrentDay_total.setMinimumSize(QSize(100, 0))
        self.profitCurrentDay_total.setMaximumSize(QSize(100, 16777215))
        self.profitCurrentDay_total.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.profitCurrentDay_total.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.profitCurrentDay_total.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.profitCurrentDay_total)

        self.profitCurrentDay_long = QLabel(self.layoutWidget)
        self.profitCurrentDay_long.setObjectName(u"profitCurrentDay_long")
        self.profitCurrentDay_long.setMinimumSize(QSize(100, 0))
        self.profitCurrentDay_long.setMaximumSize(QSize(100, 16777215))
        self.profitCurrentDay_long.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.profitCurrentDay_long.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.profitCurrentDay_long.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.profitCurrentDay_long)

        self.profitCurrentDay_short = QLabel(self.layoutWidget)
        self.profitCurrentDay_short.setObjectName(u"profitCurrentDay_short")
        self.profitCurrentDay_short.setMinimumSize(QSize(100, 0))
        self.profitCurrentDay_short.setMaximumSize(QSize(100, 16777215))
        self.profitCurrentDay_short.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.profitCurrentDay_short.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"border: 1px solid rgb(121, 121, 121);")
        self.profitCurrentDay_short.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.profitCurrentDay_short)


        self.verticalLayout.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_13.addLayout(self.verticalLayout)


        self.verticalLayout_8.addLayout(self.horizontalLayout_13)

        self.tradesView = QTableView(self.layoutWidget)
        self.tradesView.setObjectName(u"tradesView")
        self.tradesView.setStyleSheet(u"QTableView {\n"
"	border: 1px solid rgb(121, 121, 121);\n"
"}\n"
"\n"
"QTableView::item {\n"
"	border-bottom: 1px solid rgb(121, 121, 121);\n"
"	color : white;\n"
"	font: 10pt \"Courier New\";\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"	border: none;\n"
"	background-color: rgb(139, 139, 139);\n"
"}\n"
"")
        self.tradesView.setFrameShape(QFrame.Shape.StyledPanel)
        self.tradesView.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tradesView.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.tradesView.setAutoScroll(True)
        self.tradesView.setProperty("showDropIndicator", True)
        self.tradesView.setAlternatingRowColors(False)
        self.tradesView.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tradesView.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tradesView.setShowGrid(False)
        self.tradesView.horizontalHeader().setCascadingSectionResizes(True)
        self.tradesView.horizontalHeader().setMinimumSectionSize(40)
        self.tradesView.horizontalHeader().setDefaultSectionSize(112)
        self.tradesView.horizontalHeader().setHighlightSections(False)
        self.tradesView.horizontalHeader().setProperty("showSortIndicator", False)
        self.tradesView.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.tradesView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.profileButton.setDefault(False)
        self.settingsButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TradingDiary", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Pnl:", None))
        self.profileButton.setText("")
        self.settingsButton.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Tiker:", None))
        self.tickerEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BTCUSDT", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Starting Date:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Final Date:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Direction Order:", None))
        self.directionSelector.setItemText(0, QCoreApplication.translate("MainWindow", u"No Matter", None))
        self.directionSelector.setItemText(1, QCoreApplication.translate("MainWindow", u"Long", None))
        self.directionSelector.setItemText(2, QCoreApplication.translate("MainWindow", u"Short", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Profit/Loss:", None))
        self.profitSelector.setItemText(0, QCoreApplication.translate("MainWindow", u"No Matter", None))
        self.profitSelector.setItemText(1, QCoreApplication.translate("MainWindow", u"Profit", None))
        self.profitSelector.setItemText(2, QCoreApplication.translate("MainWindow", u"Loss", None))

        self.refreshButton.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Total trades", None))
        self.totalTrades_total.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.totalTrades_long.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.totalTrades_short.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Average net profit", None))
        self.avgNetProfit_total.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.avgNetProfit_long.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.avgNetProfit_short.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Total profit", None))
        self.totalProfit_total.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.totalProfit_long.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.totalProfit_short.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Profitable trades", None))
        self.profitTrades_total.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.profitTrades_long.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.profitTrades_short.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Losing trades", None))
        self.losingTrades_total.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.losingTrades_long.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.losingTrades_short.setText(QCoreApplication.translate("MainWindow", u"Short", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Profit current day", None))
        self.profitCurrentDay_total.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.profitCurrentDay_long.setText(QCoreApplication.translate("MainWindow", u"Long", None))
        self.profitCurrentDay_short.setText(QCoreApplication.translate("MainWindow", u"Short", None))
    # retranslateUi

