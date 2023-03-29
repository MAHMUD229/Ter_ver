from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Tsk3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 699)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.46729, y2:1, stop:0 rgba(115, 125, 254, 255), stop:1 rgba(255, 202, 201, 255))")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgba(0,0,0,10);\n"
"border: 2px solid rgba(143, 184, 237, 1);\n"
"border-radius: 7px;\n"
"\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 24, 105);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 24, 105);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 24, 105);")
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setObjectName("spinBox")
        self.verticalLayout.addWidget(self.splitter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 24, 105);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidgetIn = QtWidgets.QTableWidget(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidgetIn.setFont(font)
        self.tableWidgetIn.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 24, 105);")
        self.tableWidgetIn.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidgetIn.setAutoScroll(True)
        self.tableWidgetIn.setProperty("showDropIndicator", True)
        self.tableWidgetIn.setDragEnabled(False)
        self.tableWidgetIn.setDragDropOverwriteMode(True)
        self.tableWidgetIn.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidgetIn.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidgetIn.setShowGrid(True)
        self.tableWidgetIn.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidgetIn.setCornerButtonEnabled(True)
        self.tableWidgetIn.setObjectName("tableWidgetIn")
        self.tableWidgetIn.setColumnCount(2)
        self.tableWidgetIn.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetIn.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetIn.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetIn.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetIn.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetIn.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetIn.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetIn.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetIn.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetIn.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetIn.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetIn.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetIn.setHorizontalHeaderItem(1, item)
        self.tableWidgetIn.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_3.addWidget(self.tableWidgetIn)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 24, 105);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 24, 105);")
        self.tableWidget_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setAutoScroll(False)
        self.tableWidget_2.setColumnCount(1)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.horizontalLayout_3.addWidget(self.tableWidget_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 24, 105);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 24, 105);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Tsk3.jpg"))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 24, 105);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Tsk3_2.png"))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 24, 105);")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("Tsk3_3.png"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Back = QtWidgets.QPushButton(self.frame_2)
        self.Back.setMinimumSize(QtCore.QSize(200, 81))
        self.Back.setMaximumSize(QtCore.QSize(290, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Back.setFont(font)
        self.Back.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.Back.setStyleSheet("color: rgb(0, 24, 105);\n"
"background-color: rgb(255, 255, 255);")
        self.Back.setObjectName("Back")
        self.horizontalLayout.addWidget(self.Back)
        self.getResTsk3 = QtWidgets.QPushButton(self.frame_2)
        self.getResTsk3.setMinimumSize(QtCore.QSize(200, 81))
        self.getResTsk3.setMaximumSize(QtCore.QSize(290, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.getResTsk3.setFont(font)
        self.getResTsk3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.getResTsk3.setStyleSheet("color: rgb(0, 24, 105);\n"
"background-color: rgb(255, 255, 255);")
        self.getResTsk3.setObjectName("getResTsk3")
        self.horizontalLayout.addWidget(self.getResTsk3)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 24, 105);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.res_P_A = QtWidgets.QLineEdit(self.frame_2)
        self.res_P_A.setMinimumSize(QtCore.QSize(200, 81))
        self.res_P_A.setMaximumSize(QtCore.QSize(290, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.res_P_A.setFont(font)
        self.res_P_A.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.res_P_A.setStyleSheet("color: rgb(0, 0, 0);\n"
"color: rgb(0, 24, 105);\n"
"background-color: white;")
        self.res_P_A.setInputMask("")
        self.res_P_A.setText("")
        self.res_P_A.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.res_P_A.setAlignment(QtCore.Qt.AlignCenter)
        self.res_P_A.setDragEnabled(False)
        self.res_P_A.setReadOnly(True)
        self.res_P_A.setPlaceholderText("")
        self.res_P_A.setObjectName("res_P_A")
        self.horizontalLayout.addWidget(self.res_P_A)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_8.setText(_translate("MainWindow", "Расчет полной вероятности и формулы Байеса"))
        self.label.setText(_translate("MainWindow", "Введите число событий"))
        self.label_2.setText(_translate("MainWindow", "Введите вероятности гипотез P(Hi) и условных вероятностей P_Hi(A)"))
        self.tableWidgetIn.setSortingEnabled(False)
        item = self.tableWidgetIn.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidgetIn.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidgetIn.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidgetIn.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidgetIn.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidgetIn.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidgetIn.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidgetIn.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidgetIn.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidgetIn.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidgetIn.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "P(Hi)"))
        item = self.tableWidgetIn.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "P_Hi(A)"))
        self.label_3.setText(_translate("MainWindow", "Вычисленные условные вероятности P_A(Hi)"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "P_A(Hi)"))
        self.label_9.setText(_translate("MainWindow", "Блок расчетных формул"))
        self.Back.setText(_translate("MainWindow", "Назад"))
        self.getResTsk3.setText(_translate("MainWindow", "Расчитать"))
        self.label_4.setText(_translate("MainWindow", "Полная\n"
" вероятность:"))

