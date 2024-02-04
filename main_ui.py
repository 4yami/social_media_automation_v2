# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1139, 623)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setIconSize(QSize(64, 64))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sidebar_widget = QWidget(self.centralwidget)
        self.sidebar_widget.setObjectName(u"sidebar_widget")
        sizePolicy.setHeightForWidth(self.sidebar_widget.sizePolicy().hasHeightForWidth())
        self.sidebar_widget.setSizePolicy(sizePolicy)
        self.sidebar_widget.setMinimumSize(QSize(120, 0))
        self.sidebar_widget.setMaximumSize(QSize(200, 16777215))
        self.verticalLayout = QVBoxLayout(self.sidebar_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo_label = QLabel(self.sidebar_widget)
        self.logo_label.setObjectName(u"logo_label")
        self.logo_label.setMinimumSize(QSize(50, 50))
        self.logo_label.setMaximumSize(QSize(50, 50))
        self.logo_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.logo_label, 0, Qt.AlignHCenter)

        self.home_btn = QPushButton(self.sidebar_widget)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setCheckable(True)
        self.home_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_btn)

        self.account_btn = QPushButton(self.sidebar_widget)
        self.account_btn.setObjectName(u"account_btn")
        self.account_btn.setCheckable(True)
        self.account_btn.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.account_btn)

        self.verticalSpacer = QSpacerItem(20, 504, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.exit_btn = QPushButton(self.sidebar_widget)
        self.exit_btn.setObjectName(u"exit_btn")

        self.verticalLayout.addWidget(self.exit_btn)


        self.horizontalLayout_2.addWidget(self.sidebar_widget)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.main_widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.page_widget = QStackedWidget(self.main_widget)
        self.page_widget.setObjectName(u"page_widget")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.horizontalLayout_3 = QHBoxLayout(self.home_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.image_label = QLabel(self.home_page)
        self.image_label.setObjectName(u"image_label")
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QSize(125, 0))
        font = QFont()
        font.setPointSize(15)
        self.image_label.setFont(font)
        self.image_label.setAutoFillBackground(False)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.image_label)

        self.image_nav_label = QLabel(self.home_page)
        self.image_nav_label.setObjectName(u"image_nav_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.image_nav_label.sizePolicy().hasHeightForWidth())
        self.image_nav_label.setSizePolicy(sizePolicy2)
        self.image_nav_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.image_nav_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_btn = QPushButton(self.home_page)
        self.add_btn.setObjectName(u"add_btn")

        self.horizontalLayout.addWidget(self.add_btn)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.previous_btn = QPushButton(self.home_page)
        self.previous_btn.setObjectName(u"previous_btn")

        self.horizontalLayout.addWidget(self.previous_btn)

        self.next_btn = QPushButton(self.home_page)
        self.next_btn.setObjectName(u"next_btn")

        self.horizontalLayout.addWidget(self.next_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.remove_btn = QPushButton(self.home_page)
        self.remove_btn.setObjectName(u"remove_btn")

        self.horizontalLayout.addWidget(self.remove_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.post_text_input = QTextEdit(self.home_page)
        self.post_text_input.setObjectName(u"post_text_input")
        self.post_text_input.setMaximumSize(QSize(600000, 120))

        self.verticalLayout_2.addWidget(self.post_text_input)

        self.post_btn = QPushButton(self.home_page)
        self.post_btn.setObjectName(u"post_btn")

        self.verticalLayout_2.addWidget(self.post_btn)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.home_table = QTableWidget(self.home_page)
        self.home_table.setObjectName(u"home_table")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.home_table.sizePolicy().hasHeightForWidth())
        self.home_table.setSizePolicy(sizePolicy3)
        self.home_table.setMaximumSize(QSize(250, 16777215))

        self.horizontalLayout_3.addWidget(self.home_table)

        self.page_widget.addWidget(self.home_page)
        self.account_page = QWidget()
        self.account_page.setObjectName(u"account_page")
        self.verticalLayout_3 = QVBoxLayout(self.account_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.social_media_label = QLabel(self.account_page)
        self.social_media_label.setObjectName(u"social_media_label")

        self.horizontalLayout_8.addWidget(self.social_media_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.facebook_group_rbtn = QRadioButton(self.account_page)
        self.facebook_group_rbtn.setObjectName(u"facebook_group_rbtn")

        self.horizontalLayout_9.addWidget(self.facebook_group_rbtn)

        self.rbtn2 = QRadioButton(self.account_page)
        self.rbtn2.setObjectName(u"rbtn2")

        self.horizontalLayout_9.addWidget(self.rbtn2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.link_name_label = QLabel(self.account_page)
        self.link_name_label.setObjectName(u"link_name_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.link_name_label.sizePolicy().hasHeightForWidth())
        self.link_name_label.setSizePolicy(sizePolicy4)

        self.horizontalLayout_10.addWidget(self.link_name_label)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.link_name_input = QLineEdit(self.account_page)
        self.link_name_input.setObjectName(u"link_name_input")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.link_name_input.sizePolicy().hasHeightForWidth())
        self.link_name_input.setSizePolicy(sizePolicy5)
        self.link_name_input.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_11.addWidget(self.link_name_input)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.link_label = QLabel(self.account_page)
        self.link_label.setObjectName(u"link_label")
        sizePolicy4.setHeightForWidth(self.link_label.sizePolicy().hasHeightForWidth())
        self.link_label.setSizePolicy(sizePolicy4)

        self.horizontalLayout_5.addWidget(self.link_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.link_input = QLineEdit(self.account_page)
        self.link_input.setObjectName(u"link_input")
        sizePolicy5.setHeightForWidth(self.link_input.sizePolicy().hasHeightForWidth())
        self.link_input.setSizePolicy(sizePolicy5)
        self.link_input.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_6.addWidget(self.link_input)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.add_link_btn = QPushButton(self.account_page)
        self.add_link_btn.setObjectName(u"add_link_btn")

        self.horizontalLayout_12.addWidget(self.add_link_btn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.account_table = QTableWidget(self.account_page)
        self.account_table.setObjectName(u"account_table")
        self.account_table.setEditTriggers(QAbstractItemView.AnyKeyPressed|QAbstractItemView.EditKeyPressed)
        self.account_table.setSortingEnabled(False)
        self.account_table.setCornerButtonEnabled(False)
        self.account_table.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.account_table)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.edit_link_btn = QPushButton(self.account_page)
        self.edit_link_btn.setObjectName(u"edit_link_btn")

        self.horizontalLayout_7.addWidget(self.edit_link_btn)

        self.remove_link_btn = QPushButton(self.account_page)
        self.remove_link_btn.setObjectName(u"remove_link_btn")

        self.horizontalLayout_7.addWidget(self.remove_link_btn)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.page_widget.addWidget(self.account_page)

        self.horizontalLayout_4.addWidget(self.page_widget)


        self.horizontalLayout_2.addWidget(self.main_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.exit_btn.clicked.connect(MainWindow.close)

        self.page_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.logo_label.setText(QCoreApplication.translate("MainWindow", u"V1.0.0", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.account_btn.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.exit_btn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.image_label.setText("")
        self.image_nav_label.setText("")
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.previous_btn.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.remove_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
        self.post_btn.setText(QCoreApplication.translate("MainWindow", u"Post", None))
        self.social_media_label.setText(QCoreApplication.translate("MainWindow", u"Social Media :", None))
        self.facebook_group_rbtn.setText(QCoreApplication.translate("MainWindow", u"Facebook Group", None))
        self.rbtn2.setText(QCoreApplication.translate("MainWindow", u"Radio Button 2", None))
        self.link_name_label.setText(QCoreApplication.translate("MainWindow", u"Link Name :", None))
        self.link_label.setText(QCoreApplication.translate("MainWindow", u"Link :", None))
        self.add_link_btn.setText(QCoreApplication.translate("MainWindow", u"Add link", None))
        self.edit_link_btn.setText(QCoreApplication.translate("MainWindow", u"Edit link", None))
        self.remove_link_btn.setText(QCoreApplication.translate("MainWindow", u"Remove link", None))
    # retranslateUi

