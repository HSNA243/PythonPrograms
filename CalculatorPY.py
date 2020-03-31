# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalculatorGUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import math
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 110, 403, 530))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.point = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.point.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.point.setFont(font)
        self.point.setAutoFillBackground(False)
        self.point.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.point.setObjectName("point")
        self.gridLayout.addWidget(self.point, 4, 2, 1, 1)
        self.div = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.div.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.div.setFont(font)
        self.div.setAutoFillBackground(False)
        self.div.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.div.setObjectName("div")
        self.gridLayout.addWidget(self.div, 1, 3, 1, 1)
        self.mul = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.mul.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.mul.setFont(font)
        self.mul.setAutoFillBackground(False)
        self.mul.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.mul.setObjectName("mul")
        self.gridLayout.addWidget(self.mul, 0, 3, 1, 1)
        self.B5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B5.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.B5.setFont(font)
        self.B5.setAutoFillBackground(False)
        self.B5.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.B5.setObjectName("B5")
        self.gridLayout.addWidget(self.B5, 2, 1, 1, 1)
        self.min = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.min.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.min.setFont(font)
        self.min.setAutoFillBackground(False)
        self.min.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.min.setObjectName("min")
        self.gridLayout.addWidget(self.min, 2, 3, 1, 1)
        self.Clear = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Clear.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.Clear.setFont(font)
        self.Clear.setAutoFillBackground(False)
        self.Clear.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.Clear.setObjectName("Clear")
        self.gridLayout.addWidget(self.Clear, 0, 0, 1, 1)
        self.squarex = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.squarex.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.squarex.setFont(font)
        self.squarex.setAutoFillBackground(False)
        self.squarex.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.squarex.setObjectName("squarex")
        self.gridLayout.addWidget(self.squarex, 0, 2, 1, 1)
        self.B8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B8.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.B8.setFont(font)
        self.B8.setAutoFillBackground(False)
        self.B8.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.B8.setObjectName("B8")
        self.gridLayout.addWidget(self.B8, 1, 1, 1, 1)
        self.B6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B6.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.B6.setFont(font)
        self.B6.setAutoFillBackground(False)
        self.B6.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.B6.setObjectName("B6")
        self.gridLayout.addWidget(self.B6, 2, 2, 1, 1)
        self.equal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.equal.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.equal.setFont(font)
        self.equal.setAutoFillBackground(False)
        self.equal.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.equal.setObjectName("equal")
        self.gridLayout.addWidget(self.equal, 4, 3, 1, 1)
        self.B9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B9.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.B9.setFont(font)
        self.B9.setAutoFillBackground(False)
        self.B9.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.B9.setObjectName("B9")
        self.gridLayout.addWidget(self.B9, 1, 2, 1, 1)
        self.B2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B2.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.B2.setFont(font)
        self.B2.setAutoFillBackground(False)
        self.B2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.B2.setObjectName("B2")
        self.gridLayout.addWidget(self.B2, 3, 1, 1, 1)
        self.plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.plus.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.plus.setFont(font)
        self.plus.setAutoFillBackground(False)
        self.plus.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.plus.setObjectName("plus")
        self.gridLayout.addWidget(self.plus, 3, 3, 1, 1)
        self.B7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B7.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.B7.setFont(font)
        self.B7.setAutoFillBackground(False)
        self.B7.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.B7.setObjectName("B7")
        self.gridLayout.addWidget(self.B7, 1, 0, 1, 1)
        self.B3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B3.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.B3.setFont(font)
        self.B3.setAutoFillBackground(False)
        self.B3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.B3.setObjectName("B3")
        self.gridLayout.addWidget(self.B3, 3, 2, 1, 1)
        self.rootx = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.rootx.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.rootx.setFont(font)
        self.rootx.setAutoFillBackground(False)
        self.rootx.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.rootx.setObjectName("rootx")
        self.gridLayout.addWidget(self.rootx, 0, 1, 1, 1)
        self.B1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B1.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.B1.setFont(font)
        self.B1.setAutoFillBackground(False)
        self.B1.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.B1.setObjectName("B1")
        self.gridLayout.addWidget(self.B1, 3, 0, 1, 1)
        self.B0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B0.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.B0.setFont(font)
        self.B0.setAutoFillBackground(False)
        self.B0.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.B0.setObjectName("B0")
        self.gridLayout.addWidget(self.B0, 4, 1, 1, 1)
        self.pm = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pm.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pm.setFont(font)
        self.pm.setAutoFillBackground(False)
        self.pm.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pm.setObjectName("B0")
        self.gridLayout.addWidget(self.pm, 4, 0, 1, 1)
        self.B4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.B4.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.B4.setFont(font)
        self.B4.setAutoFillBackground(False)
        self.B4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.B4.setObjectName("B4")
        self.gridLayout.addWidget(self.B4, 2, 0, 1, 1)
        self.Output = QtWidgets.QLabel(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(20, 20, 391, 81))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Output.setFont(font)
        self.Output.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Output.setObjectName("Output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.B0.clicked.connect(self.click0)
        self.B1.clicked.connect(self.click1)
        self.B2.clicked.connect(self.click2)
        self.B3.clicked.connect(self.click3)
        self.B4.clicked.connect(self.click4)
        self.B5.clicked.connect(self.click5)
        self.B6.clicked.connect(self.click6)
        self.B7.clicked.connect(self.click7)
        self.B8.clicked.connect(self.click8)
        self.B9.clicked.connect(self.click9)
        self.plus.clicked.connect(self.clickPlus)
        self.min.clicked.connect(self.clickMin)
        self.div.clicked.connect(self.clickDiv)
        self.mul.clicked.connect(self.clickMul)
        self.squarex.clicked.connect(self.clickSq)
        self.rootx.clicked.connect(self.clickRt)
        self.Clear.clicked.connect(self.clickC)
        self.equal.clicked.connect(self.clickEq)
        self.pm.clicked.connect(self.clickpm)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.point.setText(_translate("MainWindow", "."))
        self.div.setText(_translate("MainWindow", "÷"))
        self.mul.setText(_translate("MainWindow", "X"))
        self.B5.setText(_translate("MainWindow", "5"))
        self.min.setText(_translate("MainWindow", "-"))
        self.Clear.setText(_translate("MainWindow", "C"))
        self.squarex.setText(_translate("MainWindow", "X^2"))
        self.B8.setText(_translate("MainWindow", "8"))
        self.B6.setText(_translate("MainWindow", "6"))
        self.equal.setText(_translate("MainWindow", "="))
        self.B9.setText(_translate("MainWindow", "9"))
        self.B2.setText(_translate("MainWindow", "2"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.B7.setText(_translate("MainWindow", "7"))
        self.B3.setText(_translate("MainWindow", "3"))
        self.rootx.setText(_translate("MainWindow", "√x"))
        self.B1.setText(_translate("MainWindow", "1"))
        self.B0.setText(_translate("MainWindow", "0"))
        self.B4.setText(_translate("MainWindow", "4"))
        self.Output.setText(_translate("MainWindow", ""))
        self.pm.setText(_translate("MainWindow", "+/-"))

    
    def  click0(self):
        self.Output.setText(self.Output.text()+"0")
    
    def  click1(self):
        self.Output.setText(self.Output.text()+"1")

    def  click2(self):
        self.Output.setText(self.Output.text()+"2")

    def  click3(self):
        self.Output.setText(self.Output.text()+"3")

    def  click4(self):
        self.Output.setText(self.Output.text()+"4")

    def  click5(self):
        self.Output.setText(self.Output.text()+"5")

    def  click6(self):
        self.Output.setText(self.Output.text()+"6")

    def  click7(self):
        self.Output.setText(self.Output.text()+"7")

    def  click8(self):
        self.Output.setText(self.Output.text()+"8")

    def  click9(self):
        self.Output.setText(self.Output.text()+"9")

    def  clickPlus(self):
        self.Output.setText(self.Output.text()+" + ")

    def  clickMin(self):
        self.Output.setText(self.Output.text()+" - ")
    
    def  clickDiv(self):
        self.Output.setText(self.Output.text()+" / ")

    def  clickMul(self):
        self.Output.setText(self.Output.text()+" * ")

    def  clickRt(self):
        self.Output.setText(self.Output.text()+"√")

    def  clickSq(self):
        self.Output.setText(self.Output.text()+"^2")

    def  clickpm(self):
        self.Output.setText(self.Output.text()+"-")

    def  clickC(self):
        font = QtGui.QFont()
        font.setPointSize(40)
        self.Output.setFont(font)
        self.Output.setText("")

    def clickEq(self):
        s = self.Output.text()
        i = 0
        flag = True
        while i < len(s):
            if s[i] == "^" or s[i] == "√" :
                if s[i] == "^":
                    st = s[:i]
                    k = 0
                    for j in range(len(st)-1,0,-1):
                        if st[j] == " ":
                            k = j
                            break
                    if st[k+1:] != "":
                        st = st[:k] + " " +str(pow(int(st[k:]),2)) + " "
                    else:
                        st = str(pow(int(st[k:]),2))
                    s = st + s[i+3:]
                
                elif s[i] == "√":
                    sb = s[:i]
                    sf = s[i+1:]
                    k = 0
                    print (sf)
                    if sf[0] == "-":
                        flag = False
                        break
                    for j in range(len(sf)):
                        if sf[j] == " " or j == len(sf)-1:
                            k = j
                            break
                    print(k)
                    st = sf[:k+1]
                    sf = sf[k+1:]
                    print(st)
                    a = math.sqrt(int(st))
                    print("a = ",a)
                    s = sb + str(a) + sf

            i+=1
        if flag == True:
            ans = str(eval(s))
            if float(ans) > 1000000000.0:
                font = QtGui.QFont()
                font.setPointSize(17)
                self.Output.setFont(font)
                self.Output.setText("Math Error: Number too large")
            elif len(ans) > 10:
                ans = ans[:10]
                self.Output.setText(ans)
            else:
                self.Output.setText(ans)
            print(eval(s))
        else:
            self.Output.setText("ERROR")
        


        
                    



    

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
