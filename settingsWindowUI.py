# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res_rc

class Ui_Settings(object):
    def setupUi(self, Settings):
        if not Settings.objectName():
            Settings.setObjectName(u"Settings")
        Settings.resize(241, 152)
        icon = QIcon()
        icon.addFile(u":/icons/Resources/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        Settings.setWindowIcon(icon)
        Settings.setStyleSheet(u"Background-color: #444446;")
        self.layoutWidget = QWidget(Settings)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 221, 129))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.apiKey = QLineEdit(self.layoutWidget)
        self.apiKey.setObjectName(u"apiKey")
        self.apiKey.setStyleSheet(u"QLineEdit \n"
"{\n"
"border: 1px solid rgb(121, 121, 121);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"border: 1px solid rgb(255, 255, 255);\n"
"}")

        self.verticalLayout.addWidget(self.apiKey)

        self.apiSecretKey = QLineEdit(self.layoutWidget)
        self.apiSecretKey.setObjectName(u"apiSecretKey")
        self.apiSecretKey.setStyleSheet(u"QLineEdit \n"
"{\n"
"border: 1px solid rgb(121, 121, 121);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"border: 1px solid rgb(255, 255, 255);\n"
"}")

        self.verticalLayout.addWidget(self.apiSecretKey)

        self.passphrase = QLineEdit(self.layoutWidget)
        self.passphrase.setObjectName(u"passphrase")
        self.passphrase.setStyleSheet(u"QLineEdit \n"
"{\n"
"border: 1px solid rgb(121, 121, 121);\n"
"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"border: 1px solid rgb(255, 255, 255);\n"
"}")

        self.verticalLayout.addWidget(self.passphrase)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.progress = QLabel(self.layoutWidget)
        self.progress.setObjectName(u"progress")
        self.progress.setStyleSheet(u"color:rgb(255, 255, 255);\n"
"font: 10pt \"Courier New\";")
        self.progress.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.progress)

        self.saveData = QPushButton(self.layoutWidget)
        self.saveData.setObjectName(u"saveData")
        self.saveData.setMinimumSize(QSize(25, 25))
        self.saveData.setMaximumSize(QSize(16777215, 25))
        self.saveData.setStyleSheet(u"QPushButton\n"
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

        self.verticalLayout_2.addWidget(self.saveData)


        self.retranslateUi(Settings)

        QMetaObject.connectSlotsByName(Settings)
    # setupUi

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QCoreApplication.translate("Settings", u"Settings", None))
        self.apiKey.setPlaceholderText(QCoreApplication.translate("Settings", u"API key", None))
        self.apiSecretKey.setPlaceholderText(QCoreApplication.translate("Settings", u"API secret key", None))
        self.passphrase.setPlaceholderText(QCoreApplication.translate("Settings", u"passphrase", None))
        self.progress.setText("")
        self.saveData.setText(QCoreApplication.translate("Settings", u"SAVE", None))
    # retranslateUi

