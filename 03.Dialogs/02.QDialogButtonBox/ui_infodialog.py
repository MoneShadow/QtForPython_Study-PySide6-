# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'infodialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_infodialog(object):
    def setupUi(self, infodialog):
        if not infodialog.objectName():
            infodialog.setObjectName(u"infodialog")
        infodialog.resize(513, 300)
        self.verticalLayout = QVBoxLayout(infodialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.position_label = QLabel(infodialog)
        self.position_label.setObjectName(u"position_label")

        self.horizontalLayout.addWidget(self.position_label)

        self.occupation_lineedit = QLineEdit(infodialog)
        self.occupation_lineedit.setObjectName(u"occupation_lineedit")

        self.horizontalLayout.addWidget(self.occupation_lineedit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.using_os_label = QLabel(infodialog)
        self.using_os_label.setObjectName(u"using_os_label")

        self.horizontalLayout_2.addWidget(self.using_os_label)

        self.selectos_combobox = QComboBox(infodialog)
        self.selectos_combobox.addItem("")
        self.selectos_combobox.addItem("")
        self.selectos_combobox.addItem("")
        self.selectos_combobox.setObjectName(u"selectos_combobox")

        self.horizontalLayout_2.addWidget(self.selectos_combobox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.button_box = QDialogButtonBox(infodialog)
        self.button_box.setObjectName(u"button_box")
        self.button_box.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok|QDialogButtonBox.StandardButton.Open|QDialogButtonBox.StandardButton.Save|QDialogButtonBox.StandardButton.SaveAll)

        self.verticalLayout.addWidget(self.button_box)


        self.retranslateUi(infodialog)

        QMetaObject.connectSlotsByName(infodialog)
    # setupUi

    def retranslateUi(self, infodialog):
        infodialog.setWindowTitle(QCoreApplication.translate("infodialog", u"Dialog", None))
        self.position_label.setText(QCoreApplication.translate("infodialog", u"Position", None))
        self.using_os_label.setText(QCoreApplication.translate("infodialog", u"Using OS", None))
        self.selectos_combobox.setItemText(0, QCoreApplication.translate("infodialog", u"Windows", None))
        self.selectos_combobox.setItemText(1, QCoreApplication.translate("infodialog", u"Linux", None))
        self.selectos_combobox.setItemText(2, QCoreApplication.translate("infodialog", u"Mac", None))

    # retranslateUi

