# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profileWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_Profile(object):
    def setupUi(self, Profile):
        if not Profile.objectName():
            Profile.setObjectName(u"Profile")
        Profile.resize(550, 145)
        Profile.setMinimumSize(QSize(550, 145))
        Profile.setMaximumSize(QSize(550, 145))
        icon = QIcon()
        icon.addFile(u":/icons/Resources/profile.png", QSize(), QIcon.Normal, QIcon.Off)
        Profile.setWindowIcon(icon)
        Profile.setStyleSheet(u"background-color: #444446;\n"
"color:rgb(255, 255, 255);\n"
"")
        self.layoutWidget = QWidget(Profile)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 511, 104))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(102, 102))
        self.label.setMaximumSize(QSize(102, 102))
        self.label.setStyleSheet(u"border: 1px solid rgb(121, 121, 121);")
        self.label.setPixmap(QPixmap(u":/icons/Resources/profile100x100.png"))

        self.horizontalLayout_3.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_1 = QLabel(self.layoutWidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setStyleSheet(u"border: 1px solid rgb(121, 121, 121);\n"
"color: rgb(175, 175, 175);\n"
"font: 10pt \"Courier New\";")
        self.label_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border: 1px solid rgb(121, 121, 121);\n"
"color: rgb(175, 175, 175);\n"
"font: 10pt \"Courier New\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border: 1px solid rgb(121, 121, 121);\n"
"color: rgb(175, 175, 175);\n"
"font: 10pt \"Courier New\";")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.accountEquity = QLabel(self.layoutWidget)
        self.accountEquity.setObjectName(u"accountEquity")
        self.accountEquity.setMinimumSize(QSize(128, 45))
        self.accountEquity.setMaximumSize(QSize(128, 45))
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setBold(False)
        font.setItalic(False)
        self.accountEquity.setFont(font)
        self.accountEquity.setStyleSheet(u"border: 1px solid rgb(121, 121, 121);")
        self.accountEquity.setScaledContents(False)
        self.accountEquity.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.accountEquity)

        self.available = QLabel(self.layoutWidget)
        self.available.setObjectName(u"available")
        self.available.setMinimumSize(QSize(128, 45))
        self.available.setMaximumSize(QSize(128, 45))
        font1 = QFont()
        font1.setFamilies([u"Courier New"])
        self.available.setFont(font1)
        self.available.setStyleSheet(u"border: 1px solid rgb(121, 121, 121);")
        self.available.setScaledContents(False)
        self.available.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.available)

        self.locked = QLabel(self.layoutWidget)
        self.locked.setObjectName(u"locked")
        self.locked.setMinimumSize(QSize(128, 45))
        self.locked.setMaximumSize(QSize(128, 45))
        self.locked.setFont(font1)
        self.locked.setStyleSheet(u"border: 1px solid rgb(121, 121, 121);")
        self.locked.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.locked)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Profile)

        QMetaObject.connectSlotsByName(Profile)
    # setupUi

    def retranslateUi(self, Profile):
        Profile.setWindowTitle(QCoreApplication.translate("Profile", u"Profile", None))
        self.label.setText("")
        self.label_1.setText(QCoreApplication.translate("Profile", u"Account Equity", None))
        self.label_2.setText(QCoreApplication.translate("Profile", u"Available", None))
        self.label_3.setText(QCoreApplication.translate("Profile", u"Locked", None))
        self.accountEquity.setText(QCoreApplication.translate("Profile", u"0", None))
        self.available.setText(QCoreApplication.translate("Profile", u"0", None))
        self.locked.setText(QCoreApplication.translate("Profile", u"0", None))
    # retranslateUi

