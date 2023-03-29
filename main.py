from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import sys
from Dialog import Ui_MainWindow_Dialog
from Tsk1 import Ui_MainWindow_Tsk1
from Tsk2 import Ui_MainWindow_Tsk2
from Tsk3 import Ui_MainWindow_Tsk3

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow_Dialog()
ui.setupUi(MainWindow)
MainWindow.show()

def choose_1():
    global Tsk1_window
    Tsk1_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Tsk1()
    ui.setupUi(Tsk1_window)
    MainWindow.close()
    Tsk1_window.show()

    def go_back():
        Tsk1_window.close()
        MainWindow.show()

    def get_result(self):
        q1 = ui.doubleSpinBox.value()
        q2 = ui.doubleSpinBox_2.value()
        q3 = ui.doubleSpinBox_4.value()
        q4 = ui.doubleSpinBox_3.value()
        q5 = ui.doubleSpinBox_6.value()
        q6 = ui.doubleSpinBox_5.value()


        p1 = 1-q1
        p2 = 1-q2
        p3 = 1-q3
        p4 = 1-q4
        p5 = 1-q5
        p6 = 1-q6

        result = 1 - (p1*(p2*p3 + p2*p4 + p5*p6 - p2*p3*p4 - p2*p3*p5*p6 - p2*p4*p5*p6 + p2*p3*p4*p5*p6))
        ui.lineEdit.setText(str(result))

    ui.Back.clicked.connect(go_back)
    ui.pushButton.clicked.connect(get_result)

def choose_2():
    global Tsk2_window
    Tsk2_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Tsk2()
    ui.setupUi(Tsk2_window)
    MainWindow.close()
    Tsk2_window.show()

    def go_back():
        Tsk2_window.close()
        MainWindow.show()


    def get_result():
        p1 = ui.p1.value()
        p2 = ui.p2.value()
        p3 = ui.p3.value()
        p4 = ui.p4.value()

        q1 = 1-p1
        q2 = 1-p2
        q3 = 1-p3
        q4 = 1-p4

        result1 = p1*q2*q3*q4 + q1*p2*q3*q4 + q1*p3*q2*q4 + q1*p4*q2*q3
        result2 = q1*p3*q2*q4
        result3 = p1*p2*q3*q4 + p1*p3*q2*q4 + p1*q2*q3*p4 + q1*p2*p3*q4 + q1*p2*q3*p4 + q1*q2*p3*p4
        result4 = 1 - (q1*q2*q3*q4)

        ui.a_res.setText(str(result1))
        ui.b_res.setText(str(result2))
        ui.c_res.setText(str(result3))
        ui.d_res.setText(str(result4))

    ui.back_2.clicked.connect(go_back)
    ui.result_2.clicked.connect(get_result)


def choose_3():
    global Tsk3_upd_window
    Tsk3_upd_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Tsk3()
    ui.setupUi(Tsk3_upd_window)
    MainWindow.close()
    Tsk3_upd_window.show()

    def go_back():
        Tsk3_upd_window.close()
        MainWindow.show()

    def get_result():
        n = ui.spinBox.value()
        P_H = []
        for i in range(0, n):
            P_H.append(ui.tableWidgetIn.item(i, 0))
        P_H_A = []
        for i in range(0, n):
            P_H_A.append(ui.tableWidgetIn.item(i, 1))
        P_A = 0.0
        for i in range(0, n):
            P_A += float(P_H[i].text()) * float(P_H_A[i].text())

        #sum = 0
#
        #for i in range(0, n):
        #    sum = sum + int(P_H[i])
#
        #if sum == 1:
        #    for i in range(0, n):
        #        ui.tableWidget_2.setItem(i, 0, QTableWidgetItem(str((float(P_H[i].text()) * float(P_H_A[i].text())) / P_A)))
        #        ui.res_P_A.setText(str(P_A))
        #    sum = 0
        #else:
        #    ui.res_P_A.setText('Wrong data')
        #    sum = 0

        for i in range(0, n):
            ui.tableWidget_2.setItem(i, 0, QTableWidgetItem(str((float(P_H[i].text()) * float(P_H_A[i].text())) / P_A)))
            ui.res_P_A.setText(str(P_A))

    ui.Back.clicked.connect(go_back)
    ui.getResTsk3.clicked.connect(get_result)


ui.Tsk1.clicked.connect(choose_1)
ui.Tsk2.clicked.connect(choose_2)
ui.Tsk3.clicked.connect(choose_3)
sys.exit(app.exec_())