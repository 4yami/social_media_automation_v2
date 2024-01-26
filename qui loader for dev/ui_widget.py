# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(366, 179)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.full_name_label = QLabel(Widget)
        self.full_name_label.setObjectName(u"full_name_label")

        self.horizontalLayout.addWidget(self.full_name_label)

        self.full_name_line_edit = QLineEdit(Widget)
        self.full_name_line_edit.setObjectName(u"full_name_line_edit")

        self.horizontalLayout.addWidget(self.full_name_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.occupation_label = QLabel(Widget)
        self.occupation_label.setObjectName(u"occupation_label")

        self.horizontalLayout_2.addWidget(self.occupation_label)

        self.occupation_line_edit = QLineEdit(Widget)
        self.occupation_line_edit.setObjectName(u"occupation_line_edit")

        self.horizontalLayout_2.addWidget(self.occupation_line_edit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.push_button = QPushButton(Widget)
        self.push_button.setObjectName(u"push_button")

        self.verticalLayout.addWidget(self.push_button)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.full_name_label.setText(QCoreApplication.translate("Widget", u"full name :", None))
        self.occupation_label.setText(QCoreApplication.translate("Widget", u"Occupation :", None))
        self.push_button.setText(QCoreApplication.translate("Widget", u"PushButton", None))
    # retranslateUi

