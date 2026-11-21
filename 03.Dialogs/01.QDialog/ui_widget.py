# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(400, 92)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_button = QPushButton(Widget)
        self.input_button.setObjectName(u"input_button")

        self.verticalLayout.addWidget(self.input_button)

        self.info_label = QLabel(Widget)
        self.info_label.setObjectName(u"info_label")

        self.verticalLayout.addWidget(self.info_label)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Dialog", None))
        self.input_button.setText(QCoreApplication.translate("Widget", u"\u8bf7\u586b\u5199\u57fa\u7840\u4fe1\u606f", None))
        self.info_label.setText(QCoreApplication.translate("Widget", u"\u57fa\u7840\u4fe1\u606f\uff1a", None))
    # retranslateUi

