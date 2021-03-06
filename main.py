import sys
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from supermarket import Supermarket

class Ui_MainWindow(object):

    def __init__(self):
        self.load_data()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LeftLayout = QtWidgets.QVBoxLayout()
        self.LeftLayout.setObjectName("LeftLayout")
        self.ListLayout = QtWidgets.QVBoxLayout()
        self.ListLayout.setObjectName("ListLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)     

        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())

        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setBaseSize(QtCore.QSize(0, 350))

        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        self.tableWidget.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('Produto'))
        self.tableWidget.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem('Preço'))
        self.tableWidget.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem('Remover produto'))

        self.tableWidget.cellClicked.connect(self.remove_row)

        self.ListLayout.addWidget(self.tableWidget)
        self.LeftLayout.addLayout(self.ListLayout)
        self.MoneyNotesLayout = QtWidgets.QHBoxLayout()
        self.MoneyNotesLayout.setObjectName("MoneyNotesLayout")
        self.Layout_200 = QtWidgets.QVBoxLayout()
        self.Layout_200.setObjectName("Layout_200")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(100, 50))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("./assets/200.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.Layout_200.addWidget(self.label_3)
        self.label_200 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_200.setFont(font)
        self.label_200.setScaledContents(True)
        self.label_200.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_200.setObjectName("label_200")
        self.Layout_200.addWidget(self.label_200)
        self.MoneyNotesLayout.addLayout(self.Layout_200)
        self.Layout_100 = QtWidgets.QVBoxLayout()
        self.Layout_100.setObjectName("Layout_100")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(100, 50))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("./assets/100.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.Layout_100.addWidget(self.label_4)
        self.label_100 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_100.setFont(font)
        self.label_100.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_100.setObjectName("label_100")
        self.Layout_100.addWidget(self.label_100)
        self.MoneyNotesLayout.addLayout(self.Layout_100)
        self.Layout_50 = QtWidgets.QVBoxLayout()
        self.Layout_50.setObjectName("Layout_50")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(100, 50))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./assets/50.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.Layout_50.addWidget(self.label_5)
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_50.setFont(font)
        self.label_50.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_50.setObjectName("label_50")
        self.Layout_50.addWidget(self.label_50)
        self.MoneyNotesLayout.addLayout(self.Layout_50)
        self.Layout_20 = QtWidgets.QVBoxLayout()
        self.Layout_20.setObjectName("Layout_20")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setMaximumSize(QtCore.QSize(100, 50))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("./assets/20.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.Layout_20.addWidget(self.label_7)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_20.setObjectName("label_20")
        self.Layout_20.addWidget(self.label_20)
        self.MoneyNotesLayout.addLayout(self.Layout_20)
        self.Layout_10 = QtWidgets.QVBoxLayout()
        self.Layout_10.setObjectName("Layout_10")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMaximumSize(QtCore.QSize(100, 50))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("./assets/10.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.Layout_10.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_10.setObjectName("label_10")
        self.Layout_10.addWidget(self.label_10)
        self.MoneyNotesLayout.addLayout(self.Layout_10)
        self.Layout_5 = QtWidgets.QVBoxLayout()
        self.Layout_5.setObjectName("Layout_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setMaximumSize(QtCore.QSize(100, 50))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("./assets/5.jpg"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.Layout_5.addWidget(self.label_11)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.Layout_5.addWidget(self.label_5)
        self.MoneyNotesLayout.addLayout(self.Layout_5)
        self.Layout_2 = QtWidgets.QVBoxLayout()
        self.Layout_2.setObjectName("Layout_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setMaximumSize(QtCore.QSize(100, 50))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("./assets/2.jpg"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.Layout_2.addWidget(self.label_13)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.Layout_2.addWidget(self.label_2)
        self.MoneyNotesLayout.addLayout(self.Layout_2)
        self.LeftLayout.addLayout(self.MoneyNotesLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 1, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.LeftLayout.addItem(spacerItem)
        self.MoneyCoinsLayout = QtWidgets.QHBoxLayout()
        self.MoneyCoinsLayout.setObjectName("MoneyCoinsLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.MoneyCoinsLayout.addItem(spacerItem1)
        self.Layout_1 = QtWidgets.QVBoxLayout()
        self.Layout_1.setObjectName("Layout_1")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMaximumSize(QtCore.QSize(75, 50))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("./assets/1.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.Layout_1.addWidget(self.label_8)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_1.setObjectName("label_1")
        self.Layout_1.addWidget(self.label_1)
        self.MoneyCoinsLayout.addLayout(self.Layout_1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setMaximumSize(QtCore.QSize(50, 50))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("./assets/0.5.png"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_050 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_050.setFont(font)
        self.label_050.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_050.setObjectName("label_050")
        self.verticalLayout_2.addWidget(self.label_050)
        self.MoneyCoinsLayout.addLayout(self.verticalLayout_2)
        self.Layout_025 = QtWidgets.QVBoxLayout()
        self.Layout_025.setObjectName("Layout_025")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setMaximumSize(QtCore.QSize(50, 50))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("./assets/0.25.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.Layout_025.addWidget(self.label_16)
        self.label_025 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_025.setFont(font)
        self.label_025.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_025.setObjectName("label_025")
        self.Layout_025.addWidget(self.label_025)
        self.MoneyCoinsLayout.addLayout(self.Layout_025)
        self.Layout_010 = QtWidgets.QVBoxLayout()
        self.Layout_010.setObjectName("Layout_010")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setMaximumSize(QtCore.QSize(50, 50))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("./assets/0.1.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setObjectName("label_19")
        self.Layout_010.addWidget(self.label_19)
        self.label_010 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_010.setFont(font)
        self.label_010.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_010.setObjectName("label_010")
        self.Layout_010.addWidget(self.label_010)
        self.MoneyCoinsLayout.addLayout(self.Layout_010)
        self.Layout_005 = QtWidgets.QVBoxLayout()
        self.Layout_005.setObjectName("Layout_005")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setMaximumSize(QtCore.QSize(50, 50))
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("./assets/0.05.png"))
        self.label_22.setScaledContents(True)
        self.label_22.setObjectName("label_22")
        self.Layout_005.addWidget(self.label_22)
        self.label_005 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_005.setFont(font)
        self.label_005.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_005.setObjectName("label_005")
        self.Layout_005.addWidget(self.label_005)
        self.MoneyCoinsLayout.addLayout(self.Layout_005)
        self.Layout_001 = QtWidgets.QVBoxLayout()
        self.Layout_001.setObjectName("Layout_001")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setMaximumSize(QtCore.QSize(50, 50))
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("./assets/0.01.png"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.Layout_001.addWidget(self.label_23)
        self.label_001 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_001.setFont(font)
        self.label_001.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_001.setObjectName("label_001")
        self.Layout_001.addWidget(self.label_001)
        self.MoneyCoinsLayout.addLayout(self.Layout_001)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.MoneyCoinsLayout.addItem(spacerItem2)
        self.LeftLayout.addLayout(self.MoneyCoinsLayout)
        self.horizontalLayout_2.addLayout(self.LeftLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.products_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.products_ComboBox.setFont(font)
        self.products_ComboBox.setObjectName("products_ComboBox")
        self.load_ComboBox()
        self.verticalLayout.addWidget(self.products_ComboBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_product)
        self.verticalLayout.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.TotalLayouts = QtWidgets.QVBoxLayout()
        self.TotalLayouts.setObjectName("TotalLayouts")
        self.TotalProductsLayout = QtWidgets.QHBoxLayout()
        self.TotalProductsLayout.setObjectName("TotalProductsLayout")
        self.total_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.total_label.setFont(font)
        self.total_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.total_label.setObjectName("total_label")
        self.TotalProductsLayout.addWidget(self.total_label)
        self.total_products = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.total_products.setFont(font)
        self.total_products.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.total_products.setObjectName("total_products")
        self.TotalProductsLayout.addWidget(self.total_products)
        self.TotalLayouts.addLayout(self.TotalProductsLayout)
        self.TotalPaidLayout = QtWidgets.QHBoxLayout()
        self.TotalPaidLayout.setObjectName("TotalPaidLayout")
        self.TotalPaidLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TotalPaidLabel.setFont(font)
        self.TotalPaidLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.TotalPaidLabel.setObjectName("TotalPaidLabel")
        self.TotalPaidLayout.addWidget(self.TotalPaidLabel)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setMaximum(99999.99)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.doubleSpinBox.valueChanged.connect(self.set_change)
        self.TotalPaidLayout.addWidget(self.doubleSpinBox)
        self.TotalLayouts.addLayout(self.TotalPaidLayout)
        self.TotalChangeLayout = QtWidgets.QHBoxLayout()
        self.TotalChangeLayout.setObjectName("TotalChangeLayout")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.TotalChangeLayout.addWidget(self.label_25)
        self.change_value = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.change_value.setFont(font)
        self.change_value.setObjectName("change_value")
        self.TotalChangeLayout.addWidget(self.change_value)
        self.TotalLayouts.addLayout(self.TotalChangeLayout)
        self.verticalLayout.addLayout(self.TotalLayouts)
        spacerItem5 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Supermercado"))
        self.label_200.setText(_translate("MainWindow", "0"))
        self.label_100.setText(_translate("MainWindow", "0"))
        self.label_50.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.label_1.setText(_translate("MainWindow", "0"))
        self.label_050.setText(_translate("MainWindow", "0"))
        self.label_025.setText(_translate("MainWindow", "0"))
        self.label_010.setText(_translate("MainWindow", "0"))
        self.label_005.setText(_translate("MainWindow", "0"))
        self.label_001.setText(_translate("MainWindow", "0"))
        self.label.setText(_translate("MainWindow", "Produtos"))
        self.pushButton.setText(_translate("MainWindow", "Adicionar"))
        self.total_label.setText(_translate("MainWindow", "Total:"))
        self.total_products.setText(_translate("MainWindow", "R$ 00.00"))
        self.TotalPaidLabel.setText(_translate("MainWindow", "Valor pago:"))
        self.label_25.setText(_translate("MainWindow", "Troco:"))
        self.change_value.setText(_translate("MainWindow", "R$ 00.00"))

    def set_change(self):
        if self.supermarket.get_total() != 0:
            change_value = float(self.doubleSpinBox.value()) - self.supermarket.get_total()
            self.change_value.setText('R$ {:.2f}'.format(change_value))

            change_count = self.supermarket.calculate_number_of_coins(change_value)
            
            for note in change_count.keys():
                if note == 200.0:
                    self.label_200.setText(str(change_count[note]))
                elif note == 100.0:
                    self.label_100.setText(str(change_count[note]))
                elif note == 50.0:
                    self.label_50.setText(str(change_count[note]))
                elif note == 20.0:
                    self.label_20.setText(str(change_count[note]))
                elif note == 10.0:
                    self.label_10.setText(str(change_count[note]))
                elif note == 5.0:
                    self.label_5.setText(str(change_count[note]))
                elif note == 2.0:
                    self.label_2.setText(str(change_count[note]))
                elif note == 1.0:
                    self.label_1.setText(str(change_count[note]))
                elif note == 0.5:
                    self.label_050.setText(str(change_count[note]))
                elif note == 0.25:
                    self.label_025.setText(str(change_count[note]))
                elif note == 0.10:
                    self.label_010.setText(str(change_count[note]))
                elif note == 0.05:
                    self.label_005.setText(str(change_count[note]))
                elif note == 0.01:
                    self.label_001.setText(str(change_count[note]))

    def remove_row(self, row, column):
        if column == 2:
            self.supermarket.change_value(float(self.tableWidget.item(row, column - 1).text().split()[1]) * (-1))
            self.tableWidget.removeRow(row)
            self.total_products.setText('R$ {:.2f}'.format(self.supermarket.get_total()))
            self.doubleSpinBox.setMinimum(self.supermarket.get_total())

    def add_product(self):
        if self.products_ComboBox.currentText() != "":
            self.tableWidget.insertRow(self.tableWidget.rowCount())
            
            product = QtWidgets.QTableWidgetItem(self.products_ComboBox.currentText())
            product.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 0, product)
            
            price = QtWidgets.QTableWidgetItem('R$ {:.2f}'.format(self.products[self.products_ComboBox.currentText()]))
            price.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 1, price)
            
            remove_icon = QtWidgets.QTableWidgetItem()
            icon = QtGui.QIcon('./assets/x.png')
            remove_icon.setIcon(icon)
            remove_icon.setTextAlignment(QtCore.Qt.AlignHCenter)

            self.tableWidget.setItem(self.tableWidget.rowCount() - 1, 2, remove_icon)

            self.supermarket.change_value(float(self.products[self.products_ComboBox.currentText()]))        
            self.total_products.setText('R$ {:.2f}'.format(self.supermarket.get_total()))
            self.doubleSpinBox.setMinimum(self.supermarket.get_total())

    def load_ComboBox(self):
        self.products_ComboBox.addItem(None)
        for product in self.products.keys():
            self.products_ComboBox.addItem(product)
        
    def load_data(self):
        df = pd.read_csv('./dataset/Produtos.csv', delimiter=";", encoding='latin-1')
        df.columns = ['Produtos', 'Preços']
        df['Preços'] = df['Preços'].str.replace(',', '.').astype(float)
        self.products = dict(df.values.tolist())
        self.supermarket = Supermarket()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    sys.exit(app.exec_())